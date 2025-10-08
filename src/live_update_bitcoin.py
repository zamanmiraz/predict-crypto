import threading
import time
import websocket
import json

stop_event = threading.Event()

def on_message(ws, message):
    data = json.loads(message)
    if data.get("event") == "trade":
        print(data["data"])

def on_open(ws):
    ws.send(json.dumps({
        "event": "bts:subscribe",
        "data": {"channel": "live_trades_btcusd"}
    }))

def run_ws():
    ws = websocket.WebSocketApp(
        "wss://ws.bitstamp.net",
        on_open=on_open,
        on_message=on_message
    )
    while not stop_event.is_set():
        ws.run_forever()
        time.sleep(5)  # reconnect delay if disconnected
    print("WebSocket stopped.")

if __name__ == "__main__":
    thread = threading.Thread(target=run_ws)
    thread.start()

    # Let it run for 60 seconds
    time.sleep(60)
    stop_event.set()
