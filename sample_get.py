from locust import HttpUser, between, task
 
baseEndpoint = "https://run.mocky.io/v3/"
 
class ScriptUser(HttpUser):
   wait_time = between(5, 15)
  
   @task
   def on_start(self):
       response = self.client.request(
           method="GET",
           url=baseEndpoint + "a3017754-7aba-4a0e-a032-dc5cf96a5b95",
           name="get_mocky",
        )