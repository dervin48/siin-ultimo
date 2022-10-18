from datetime import datetime

from crum import get_current_request
from django.db import models
from django.forms import model_to_dict

from core.security.choices import LOGIN_TYPE
from core.user.models import User


class AccessUsers(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_joined = models.DateField(default=datetime.now)
    time_joined = models.TimeField(default=datetime.now)
    ip_address = models.CharField(max_length=50)
    type = models.CharField(max_length=15, choices=LOGIN_TYPE, default=LOGIN_TYPE[0][0])

    def __str__(self):
        return self.ip_address

    def toJSON(self):
        item = model_to_dict(self)
        item['type'] = {'id': self.type, 'name': self.get_type_display()}
        item['user'] = self.user.toJSON()
        item['date_joined'] = self.date_joined.strftime('%Y-%m-%d')
        item['time_joined'] = self.time_joined.strftime('%H:%M:%S')
        return item

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        try:
            request = get_current_request()
            self.ip_address = request.META['REMOTE_ADDR']
        except:
            pass
        super(AccessUsers, self).save()

    class Meta:
        verbose_name = 'Acceso de Usuario'
        verbose_name_plural = 'Accesos de Usuarios'
        default_permissions = ()
        permissions = (
            ('view_access_users', 'Can view Acceso de Usuario'),
            ('delete_access_users', 'Can delete Acceso de Usuario'),
        )
        ordering = ['id']
