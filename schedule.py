# Reserbot
import controller


app_controller = controller.Controller()

if app_controller.is_workday():
    # miembros del equipo no disponibles
    app_controller.schedule_message_unavailable_members()
    # miembro que lidera la daily hoy
    app_controller.schedule_message_daily_leader()
    # recordatorio de reuniones que ocurren hoy
    app_controller.schedule_message_meetings()
