import flet as ft
import requests

def main(page: ft.Page):
    page.title = "Free Stream Controller"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # PASTE YOUR GITHUB DETAILS HERE
    GITHUB_TOKEN = "PASTE_YOUR_TOKEN_FROM_STEP_1"
    REPO_OWNER = "YOUR_GITHUB_USERNAME"
    REPO_NAME = "youtube-247-stream"

    def trigger_stream(e):
        status_text.value = "Sending command..."
        page.update()
        
        url = f"https://github.com{REPO_OWNER}/{REPO_NAME}/dispatches"
        headers = {
            "Authorization": f"token {GITHUB_TOKEN}",
            "Accept": "application/vnd.github.v3+json"
        }
        data = {"event_type": "start_live_stream"}
        
        try:
            response = requests.post(url, json=data, headers=headers)
            if response.status_code == 204:
                status_text.value = "🟢 Stream Triggered Successfully!"
                status_text.color = "green"
            else:
                status_text.value = f"🔴 Failed: Code {response.status_code}"
                status_text.color = "red"
        except Exception as ex:
            status_text.value = "Error connecting to GitHub"
            status_text.color = "red"
        page.update()

    status_text = ft.Text("Status: Disconnected", size=16, weight="bold")
    
    page.add(
        ft.Card(
            content=ft.Container(
                content=ft.Column([
                    ft.Icon(ft.icons.LIVE_TV, size=50, color="blue"),
                    ft.Text("AI Live Stream Control", size=22, weight="bold"),
                    ft.Divider(),
                    ft.ElevatedButton(
                        "🚀 Start 24/7 Stream", 
                        on_click=trigger_stream,
                        style=ft.ButtonStyle(bgcolor="blue", color="white")
                    ),
                    status_text
                ], alignment="center", horizontal_alignment="center"),
                padding=30
            )
        )
    )

ft.app(target=main)
