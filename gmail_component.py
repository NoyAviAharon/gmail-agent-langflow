from langflow.custom import Component
from langflow.io import MessageTextInput, Output
from langflow.field_typing import Tool
from langchain.tools import StructuredTool
from pydantic import BaseModel, Field
import base64
from email.mime.text import MIMEText
import requests


class GmailTool(Component):
    display_name = "Gmail Tool"
    description = "Gmail tool for sending emails"
    icon = "mail"

    inputs = [
        MessageTextInput(
            name="client_id",
            display_name="Client ID",
            info="Google OAuth Client ID",
        ),
        MessageTextInput(
            name="client_secret",
            display_name="Client Secret",
            info="Google OAuth Client Secret",
        ),
        MessageTextInput(
            name="refresh_token",
            display_name="Refresh Token",
            info="Google OAuth Refresh Token",
        ),
    ]

    outputs = [
        Output(display_name="Tool", name="tool", method="build_tool"),
    ]

    def build_tool(self) -> Tool:
        class EmailInput(BaseModel):
            to_email: str = Field(description="The recipient email address")
            subject: str = Field(description="The email subject line")
            body: str = Field(description="The email body content")

        def send_email_func(to_email: str, subject: str, body: str) -> str:
            try:
                token_url = "https://oauth2.googleapis.com/token"
                token_payload = {
                    "client_id": self.client_id,
                    "client_secret": self.client_secret,
                    "refresh_token": self.refresh_token,
                    "grant_type": "refresh_token",
                }
                token_response = requests.post(token_url, data=token_payload)
                access_token = token_response.json()["access_token"]

                message = MIMEText(body)
                message["to"] = to_email
                message["subject"] = subject
                raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode("utf-8")

                url = "https://gmail.googleapis.com/gmail/v1/users/me/messages/send"
                headers = {
                    "Authorization": f"Bearer {access_token}",
                    "Content-Type": "application/json",
                }

                response = requests.post(url, headers=headers, json={"raw": raw_message})

                if response.status_code == 200:
                    return f"Email sent successfully to {to_email}!"
                else:
                    return f"Failed to send email: {response.text}"

            except Exception as e:
                return f"Error: {str(e)}"

        return StructuredTool.from_function(
            func=send_email_func,
            name="send_email",
            description="Send an email. Use this when the user asks to send an email to someone.",
            args_schema=EmailInput,
        )