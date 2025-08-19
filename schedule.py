# Reserbot
import controllers


controller = controllers.ScheduleController()

if controller.is_workday():
    # botones de entrada/salida
    controller.schedule_message_marcar()
    # miembros del equipo no disponibles
    controller.schedule_message_unavailable_members()
    # miembro que lidera la daily hoy
    controller.schedule_message_daily_leader()
    # recordatorio de reuniones que ocurren hoy
    controller.schedule_message_meetings()
