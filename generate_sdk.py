import uvicorn
import pip
import subprocess
import os 
import yaml
import sys
import json
# from flask import Flask
# from flask_restful import Api, Resource, reqparse
import datetime
import connexion
from flask_injector import FlaskInjector
from connexion.resolver import RestyResolver

__author__ = "Lorena Mesa"
__email__ = "me@lorenamesa.com"


CURRENT_DIR = os.getcwd()


def verify_eligibility(self, data):
    return {'data': 'data'}


class GenerateSdk:
    def __init__(self, requirements_file='requirements.txt', openapi_file='eligibility_api.yaml'):
        self.app = connexion.App(__name__)  # Provide the app and the directory of the docs
        self.app.add_api(openapi_file, resolver=RestyResolver('api'))
        self.injector = FlaskInjector(app=self.app.app)

        # self.swagger_url = '/api/docs'  # URL for exposing Swagger UI (without trailing '/')
        # self.api_url = '/static/swagger.json'  # Our API url (can of course be a local resource)
        self.requirements_file = requirements_file
        self.openapi_file = openapi_file
        # self.app = Flask(__name__)    
        self.__bootstrap_api__()
 
    def __bootstrap_api__(self):
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        
        open_api_config = None
        with open(f'{self.openapi_filename}') as stream:
            try:
                open_api_config = (yaml.safe_load(stream))
            except yaml.YAMLError as exc:
                print(exc)
        swaggerui_blueprint = get_swaggerui_blueprint(
            self.swagger_url,
            self.api_url,
            config = {'app_name': open_api_config['info'['title']]}
        )
        # open_api_config = None

        # if self.app.openapi_schema:
        #     return self.app.openapi_schema
        
        # with open(f'{self.openapi_filename}') as stream:
        #     try:
        #         open_api_config = (yaml.safe_load(stream))
        #     except yaml.YAMLError as exc:
        #         print(exc)

       

    def run_server(self, port=8000):
        self.app.run(self.app, host="0.0.0.0", port=8000)

        
if __name__ == "__main__":
    sdk = GenerateSdk(openapi_file='/Users/lorenamesa/Workspace/interview_prep/eligibility_api.yaml', requirements_file='requirements.txt')
    sdk.run_server()
    sdk.verify_eligibility('asdads')
    print("aosidhnasd")

    # parser = argparse.ArgumentParser(
    #     description="Python Insurance Elgibility Verifier", 
    #     usage="""Python SDK Insurance Elgbility Verifier."""
    # )

    # def validate_date_str(date_str: str) -> str:
    #     """
    #     If user provides a since parameter from the command line, this function validates the date_str provided is
    #     a valid date.

    #     :param date_str: a str representing a date in the format 'YYYY-MM-DD'
    #     """
    #     try:
    #         is_valid_date = bool(datetime.strptime(date_str, ExchangeRateAPI.DATE_STR_FORMAT))
    #         return date_str
    #     except ValueError:
    #         raise argparse.ArgumentTypeError("Invalid since date string provided, must be in format of YYYY-MM-DD.")
        
    # parser.add_argument(
    #     "-s",
    #     "--since",
    #     type=validate_date_str,
    #     required=False,
    #     help="Date string, inclusive, to retrieve the most recent US Treasury Exchange Rate quarterly data in the format of YYYY-MM-DD.",
    # )
    # args = parser.parse_args()