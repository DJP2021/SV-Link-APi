from fastapi import FastAPI
import json
import os
from supabase import create_client, Client
from supabase.client import ClientOptions

url= "https://eooateebumsuyxgqtnzj.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImVvb2F0ZWVidW1zdXl4Z3F0bnpqIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzM2NjE2MDQsImV4cCI6MjA0OTIzNzYwNH0._pqgOKldqpdHXDtqJul3FXHiP5ZfBbXwIZAtmv5md58"
supabase: Client = create_client(url, key,
  options=ClientOptions(
    postgrest_client_timeout=10,
    storage_client_timeout=10,
    schema="public",
  ))


app = FastAPI()


@app.get("/")
async def root():
    response = supabase.table("users").select("*").execute()
    return {"message": response}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.get("/system/register")
async def register(email: str=None, password: str=None):
    response = supabase.auth.sign_up(
        {"email": email, "password": password}
    )
    print(response)