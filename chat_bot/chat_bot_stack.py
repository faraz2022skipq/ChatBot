from aws_cdk import (
    Stack,
    aws_lex as lex
)
from constructs import Construct

class ChatBotStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        chatbot = lex.CfnBot(self, "WeatherAPI",
            data_privacy = {"childDirected": False},
            idle_session_ttl_in_seconds = 300,
            name = "WeatherAPI",
            role_arn = "arn:aws:iam::aws:policy/aws-service-role/LexBotPolicy")