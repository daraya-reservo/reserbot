from apscheduler.schedulers.blocking import BlockingScheduler
from utils import slack_simple_message, get_daily_leader, slack_button_message


scheduler = BlockingScheduler(timezone='America/Santiago')

@scheduler.scheduled_job('cron', day_of_week='mon-fri', hour=9, minute=45)
def daily_message():
    msg = get_daily_leader()
    if msg:
        btn = "Ir a la reunión en WhereBy"
        btn_link = "https://whereby.com/reunion-tecnica-reservo"
        slack_button_message(channel='#reservo-ti', message=msg, button_text=btn, link=btn_link)

@scheduler.scheduled_job('cron', day_of_week='wed', hour=14, minute=45)
def reu_tecnica_message():
    msg = f"Hoy hay reu técnica/cultural :abogato: a las 15:00 hrs."
    btn = "Ir a la reunión en WhereBy"
    btn_link = "https://whereby.com/reunion-tecnica-reservo"    
    slack_button_message(channel='#reservo-ti', message=msg, button_text=btn, link=btn_link)

@scheduler.scheduled_job('cron', day_of_week='mon-fri', hour=11, minute=40)
def hora_estudio_message():
    msg = f"Planeas tomar tiempo de estudio hoy? :estudio: "
    btn = "Anotarse en el excel"
    btn_link = "https://docs.google.com/spreadsheets/d/1FhaBUnW_hGk_siixvFUAjs0SZRw5iksFnSqI8XkiX3A/edit?usp=sharing"    
    slack_button_message(channel='#reservo-ti', message=msg, button_text=btn, link=btn_link)


scheduler.start()


# FOR TESTING (una vez que inicia el scheduler no considera el código debajo)
# @scheduler.scheduled_job('interval', minutes=2)
# def cron_test():
#     slack_simple_message(channel='#reserbot-shhhh', message='a')
#     slack_whereby_message(channel='#reserbot-shhhh', message='a')
#     print('This job runs every 2 minutes.')
    

# @scheduler.scheduled_job('cron', day_of_week='tue', hour=2, minute=2)
# def test2():
#     msg = get_daily_leader()
#     if msg:
#         slack_whereby_message(channel='#reserbot-shhhh', message=msg)



