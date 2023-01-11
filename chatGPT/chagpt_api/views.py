import os
import json
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

import openai
openai.api_key = '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'

def generate_response(prompt):
    model_engine = "text-davinci-003"
    prompt = (f"{prompt}")

    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message.strip()


@method_decorator(csrf_exempt,name='dispatch')
class Chatgpt(APIView):
    def post(self,request):
        params = json.loads(request.body)
        user_input = params['question']
        response = generate_response(user_input)
        return Response(['RESPONSE: ',response])




