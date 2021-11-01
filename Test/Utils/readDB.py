from connectDbSshTunnel import cursor
from connectionDb import cursor

def doctorId(self):
    cursor.execute("SELECT doctor_id FROM augmedix.ehr_integration_physician where id = 1;")
    result_getting_docId = cursor.fetchone()
    doctorID = result_getting_docId["doctor_id"]
    return doctorID


def scribedId(self):
    cursor.execute(f"SELECT distinct scribeId FROM augmedixphi.note_metadata where providerId = {self.doctorId()}")
    result_getting_scribeId = cursor.fetchone()
    scribeId = result_getting_scribeId["scribeId"]
    return scribeId


def instanceName(self):
    cursor.execute("SELECT instance_name FROM augmedix.ehr_integration_site;")
    instance_name = cursor.fetchall()
    instance_name_value = str(instance_name[0]['instance_name'])
    return instance_name_value

