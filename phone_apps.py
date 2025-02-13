class Phone:
  def __init__(self):
    self.open_apps = []
    self.close_apps = []
    self.notifcations = []

  def open_app(self, app_name):
    self.open_apps.append(app_name)
    print(f"📱 Opened {app_name}")

  def close_app(self):
    if self.open_apps:
      closed_app  = self.open_apps.pop()
      self.close_apps.append(closed_app)
      print(f"Closed app: {closed_app}")

    else:
      print("No apps are open")

  def switch_app(self):
    if len(self.open_apps) >= 2:
      self.close_apps()

      print(f"Switched to {self.open_apps[-1]}")

    else:
      print("No recently closed apps.")

  def reopen_last_closed(self):
    if self.open_apps:
      last_open = self.close_apps.pop()
      self.open_apps.append(last_open)
      print(f"🔄 Reopened {last_open}")
    else:
        print("No recently closed apps.")

  def add_notification(self, notification):
    self.notifcations.append(notification)
    print(f"🔔 New notification: {notification}")

  def read_notification(self):
    if self.notifcations:
      print(f"📩 Notification: {self.notifcations.pop(0)}")

    else:
      print("No notification")

  def phone_status(self):
    if self.open_apps:
      print(f"Open phones: {self.open_apps}")
    if self.notifcations:
      print(f"Notification: {self.notifcations}")

