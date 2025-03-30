from flask import Flask
from main import app

# This route handler is required for Vercel serverless functions
def handler(request):
    return app(request['environ'], request['start_response'])
