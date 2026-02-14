import requests
import datetime
# user_params={'token':'penpineappleapplepen','username':'butterfingers','agreeTermsOfService':'yes','notMinor':'yes'}
# pixela_endpoint="https://pixe.la/v1/users"
# response=requests.post(pixela_endpoint,json=user_params)
# print(response.status_code)
# graph_config={'id':'graph1',
#               'name': 'Coding Hours',
#               'unit':'hours',
#               'type':'float',
#               'color':'ajisai'
#                 }
headers={'X-USER-TOKEN':'penpineappleapplepen'}
graph_endpoint='https://pixe.la/v1/users/butterfingers/graphs'
# response=requests.post(graph_endpoint,json=graph_config,headers=headers)
# print(response.status_code)

#Adding a Pixel
# pixel_creation_endpoint='https://pixe.la/v1/users/butterfingers/graphs/graph1'
# pixel_config={'date':'20260213',
#               'quantity':'5'}
# response=requests.post(pixel_creation_endpoint,json=pixel_config,headers=headers)
# print(response.status_code)

#Updating a pixel
update_endpoint='https://pixe.la/v1/users/butterfingers/graphs/graph1/20260214'
# update_config={'quantity':'5'}
# response=requests.put(update_endpoint,json=update_config,headers=headers)
# print(response.status_code)


#Deleting a pixel
response=requests.delete(update_endpoint,headers=headers)
print(response.status_code)