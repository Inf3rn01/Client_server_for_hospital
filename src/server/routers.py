from server.entities.Department import routers
from server.entities.Disease import routers
from server.entities.Patients import routers
from server.entities.Post import routers
from server.entities.Reception import routers
from server.entities.Request import routers
from server.entities.Role import routers
from server.entities.Staff import routers
from server.entities.Status_request import routers
from server.entities.Treatment_status import routers
from server.entities.Type_of_disease import routers
from server.entities.Type_of_treatment import routers
from server.entities.Users import routers




router = (departments, diseases, patients, post, reception, request, role, staff, status_request,
          treatment_status, type_of_diease, type_of_treatment, users)
