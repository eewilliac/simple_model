import json
from llama_cpp import Llama


model_path = "C:\code\python\open_models\dolphin-2.5-mixtral-8x7b.Q4_0.gguf"
model_response = ""

llm = Llama(model_path=model_path,n_ctx=512, n_batch=126)
question_list = ['how much is 2 + 2.99?',
                 'what is the sound of one hand clapping?',
                 'Who was James Bond based on?',
                 'how do I learn to program a quadruped robot, like what math will I need?']
for question in question_list:
    q_string = "Question: {} Answer:".format(question)
    response_stream = llm(q_string,
              max_tokens=100, stop=["\n","Question:","Q:"],
              stream=True)
#print(json.dumps(output, indent=4))
    for response in response_stream:
        #print(json.dumps(response))
        #print(response['choices']['text']) #so this does not work somthing about list indices mst be integers or slices.
        #print(response['choices'][0])
        resp = response['choices'][0]
        #rint(type(resp))
        model_response += resp['text'] 

    print(model_response)    
    print('\n')
    model_response = ""