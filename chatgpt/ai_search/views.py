from django.shortcuts import render,redirect
from .class_chatgpt import Gpt_API


# Create your views here.
def gotoAi_search(request):
    return render(request,"search_chat.html")

def get_answer(request):
    if request.POST:
        query = request.POST.get("query")
        #print(query)
        query_final = query+". When writing down the hotel names put them in a bracket []"
        obj = Gpt_API(query_final)
        result = obj.get_result()
        result= result+"\n\nHave fun on your trip and best regards,\n\nYour Ki-Urlaub.de team"
        print("Result is = ",result)
        context={"query":query, "result":result}
        return render(request,"search_chat.html",context=context)
    else:
        return render(request,"search_chat.html")

