from django.shortcuts import render, redirect
import random
from datetime import datetime


GOLD_MAP = {
    "farm": (10,20),
    "cave": (5,10),
    "house": (2,5),
    "casino": (-50,50)
}


def index(request):
    # check if either 'gold' or 'activities' keys are not in session (yet)
    if not "gold" in request.session or "activities" not in request.session:
        # set these to initial values if that is the case!
        request.session['gold'] = 0
        request.session['activities'] = []
    return render(request, 'index.html')

def reset(request):
    request.session.clear()
    return redirect('/')

def process_gold(request):
    if request.method == 'GET':
        return redirect('/')

    building_name = request.POST['building']
    # access the correct mix/max values from the user's form submission
    building = GOLD_MAP[building_name]
    # upper case string (for message)
    building_name_upper = building_name[0].upper() + building_name[1:] 

    # calculate the correct random number for this building
    curr_gold = random.randint(building[0], building[1])

    # generate a datetime string, with the proper format, for RIGHT NOW
    now_formatted = datetime.now().strftime("%m/%d/%Y %I:%M%p")
    result = 'even'

    if curr_gold > 0:
        result = 'won'
        message = f"Earned {curr_gold} from the {building_name_upper}! ({now_formatted})"
    elif curr_gold < 0:
        result = 'lost'
        message = f"Entered a {building_name_upper} and lost {curr_gold} golds... Ouch... ({now_formatted})"
    else:
        result = 'even'
        message = f"Entered a {building_name_upper} and broke even"

    # update session gold value
    request.session['gold'] += curr_gold
    request.session['activities'].append({"message": message, "result": result})
    return redirect('/')