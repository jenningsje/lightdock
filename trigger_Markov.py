import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path == '../MarkovProprietary/pipelinestages/app/mount/input':
            # Trigger your Python function or script here
            commands = ["fetch_pdbs.ts, lightdock_setup.ts, lightdock_run.ts, ../generate_confs.ts"]
            for command in commands:
                subprocess.run(f"node {command}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

if __name__ == "__main__":
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path='../MarkovProprietary/pipelinestages/app/mount/input', recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
