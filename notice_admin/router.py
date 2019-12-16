class NoticeRouter:
    def __init__(self):
        self.model_list = ['notice_info', 'default']

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.model_list:
            return model._meta.app_label

        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.model_list:
            print('db_for_write: %s' % model._meta.app_label)
            return model._meta.app_label

        return None

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label in self.model_list or \
                obj2._meta.app_label in self.model_list:
            return True

        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if db == 'default':
            return True
        return None
