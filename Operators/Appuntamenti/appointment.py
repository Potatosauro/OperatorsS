from collections import OrderedDict

import logging
from django.db import connection
from django.contrib.auth.models import User
import datetime

LOG = logging.getLogger(__name__)


class AppointmentManager:

    def __init__(self):
        pass

    @staticmethod
    def getAvailableDays(month, year):
        """
        Ritorna la lista dei giorni disponibili in cui è possibile assegnare uno slot
        @param month => Numero del mese
        @param year => Anno
        :return
         Contiene una lista dei giorni disponibili su cui è possibile assegnare slot
         Es. ['01/03/2002', '02/03/2022']
        """













        return ['01/03/2002', '02/03/2022']

    @staticmethod
    def getAvailableSlots(day):
        """
        Ritorna la lista completa di tutti slot allocabili in un particolare giorno
        @param day => Giorno dell'anno

        Nota:
            Se:
                - operatore1 ha configurato gli slot 09:00, 09:15, 09:30, 09:45, 10:00
                - operatore2 ha configurato gli slot 09:00, 09:10, 09:20, 09:30, 09:40, 09:50, 10:00
                - operatore3 ha configurato gli slot 09:00, 09:10, 09:20, 09:30, 09:40, 09:50, 10:00
                - operatore4 ha configurato gli slot 17:00, 18:00
            Allora l'output sarà:
                ['09:00','09:10','09:15','09:20','09:30','09:40', '09:45', '09:90', '10:00', '17:00', '18:00']
        """
        return ['09:00', '09:10', '09:15', '09:20', '09:30', '09:40', '09:45', '09:90', '10:00']

    @staticmethod
    def getAvailableSlotsCount(limit_datetime):
        """
        Restituisce il numero di slot di appuntamento liberi fino alla data/ora richieste
        :param limit_datetime: Upper bound datetime (<=)
        """

        return 0

    @staticmethod
    def getAvailableOperatorsBySlot(slot_date, slot_time):
        """
        Restituisce la lista degli operatori liberi in un determinato slot
        :param slot_date => Data in cui effettuare la ricerca
        :param slot_time => Slot in cui effettuare la ricerca
        :return Lista degli operatori disponibili in quel particolare slot
        """

        free_operator = ["operatore1", "operatore2"]

        return free_operator