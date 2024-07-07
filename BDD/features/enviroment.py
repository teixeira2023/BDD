# environment.py

def before_scenario(context, scenario):
    context.cabin_light_state = None
    context.timer_active = None
    context.timer_value = None

def after_scenario(context, scenario):
    context.cabin_light_state = None
    context.timer_active = None
    context.timer_value = None
