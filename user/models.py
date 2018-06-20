# -*- coding: utf-8 -*-

from django.db import models
from time import localtime,strftime

class User(models.Model):
    id = models.AutoField(primary_key=True)
    nickname = models.CharField(db_column='nickname', max_length=100 )
    age = models.IntegerField( )
    gender = models.IntegerField(db_column='gender' )
    city = models.CharField(max_length=200 )
    location = models.CharField(max_length=200 )

    longitude = models.CharField(max_length=50 )
    latitude = models.CharField(max_length=50  )
    stepFrequency = models.IntegerField(  )
    heartBeat = models.IntegerField(  )
    stepStartTime = models.DateTimeField()
    hobby = models.CharField(max_length=200 )

    class Meta:
        managed = False
        db_table = 'user'

    @classmethod
    def getValueByNickname(self, nicknameArg, returnArg):
        try:
            obj = self.objects.get(nickname = nicknameArg)
            if returnArg == "id":
                return True, 110000, obj.id
            elif returnArg == "nickname":
                return True, 110000, obj.nickname
            elif returnArg == "age":
                return True, 110000, obj.age
            elif returnArg == "city":
                return True, 110000, obj.city
            elif returnArg == "location":
                return True, 110000, obj.location
            elif returnArg == "longitude":
                return True, 110000, obj.longitude
            elif returnArg == "latitude":
                return True, 110000, obj.latitude
            elif returnArg == "stepFrequency":
                return True, 110000, obj.stepFrequency
            elif returnArg == "heartBeat":
                return True, 110000, obj.heartBeat
            elif returnArg == "stepStartTime":
                return True, 110000, obj.stepStartTime
            else:
                return False, 110001, "  user 表中不存在该属性，returnArg 错误"
        except self.DoesNotExist:
                return False, 110002, "  user 表不存在该数据"
        except Exception as e:
                return False, 110003, str(e)

    @classmethod
    def getValueByUserId(self, userIdArg, returnArg):
        try:
            obj = self.objects.get(id = userIdArg)
            if returnArg == "id":
                return True, obj.id
            elif returnArg == "nickname":
                return True, obj.nickname
            elif returnArg == "age":
                return True, obj.age
            elif returnArg == "city":
                return True, obj.city
            elif returnArg == "location":
                return True, obj.location
            elif returnArg == "longitude":
                return True, obj.longitude
            elif returnArg == "latitude":
                return True, obj.latitude
            elif returnArg == "stepFrequency":
                return True, obj.stepFrequency
            elif returnArg == "heartBeat":
                return True, obj.heartBeat
            elif returnArg == "stepStartTime":
                return True, obj.stepStartTime
            elif returnArg == "all":
                return True, obj
            elif returnArg == "allExceptId":
                return True, obj.filter(~Q(id = userIdArg))
            else:
                return False, "  user 表中不存在该属性，returnArg 错误"
        except self.DoesNotExist:
                return False, "  user 表不存在该数据"
        except Exception as e:
                return False, str(e)

    @classmethod
    def getAllUserGPS(self, idArg):
        try:
            status, cityArg = User.getValueByUserId(idArg, "city")
            objs = User.objects.filter(city = cityArg).all()

            return True, objs
        except self.DoesNotExist:
                return False, "  user 表不存在该数据"
        except Exception as e:
            print(str(e))
            return False, str(e)

    @classmethod
    def modifyLL(self, idArg, longitudeArg, latitudeArg):
        try:
            obj = self.objects.get(id=idArg)
            obj.longitude = float(longitudeArg);
            obj.latitude = float(latitudeArg);


            obj.save()
            return True, ""
        except self.DoesNotExist:
            return False, "modify 读取 user 表错误"
        except Exception as e:
            print(str(e))
            return False, str(e)

    @classmethod
    def modifyObj(self, idArg, argName, value):
        try:
            obj = self.objects.get(id=idArg)
            if argName == "stepFrequency":
                obj.stepFrequency = value;
                obj.save()
            elif argName == "heartBeat":
                obj.heartBeat = value;
                obj.save()
            elif argName == "stepStartTime":
                obj.stepStartTime = value;
                obj.save()
            else:
                return False, "modify 读取 user 表错误"
            return True, ""
        except self.DoesNotExist:
            return False, "modify 读取 user 表错误"
        except Exception as e:
            print(str(e))
            return False, str(e)

    # @classmethod
    # def add(self, userIdArg, phoneArg):
    #     userGraderIdArg = ""
    #     try:
    #         obj = self(userId = userIdArg, userGraderId = userGraderIdArg, phone= phoneArg)
    #         obj.save()
    #         return True,110100, idArg
    #     except Exception as e:
    #         return False,110101, str(e)


    # @classmethod
    # def deleteObj(self, value):
    #     try:
    #         obj = self.objects.get(id = value)
    #         obj.delete()
    #         return True,110200, ""
    #     except self.DoesNotExist:
    #         return False, 110201, "deleteuser by | " + argName + " : " + value + " | 表错误"
    #     except Exception as e:
    #         return False, 110202, str(e)
