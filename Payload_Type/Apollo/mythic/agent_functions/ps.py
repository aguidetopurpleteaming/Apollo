from CommandBase import *
import json


class PsArguments(TaskArguments):

    def __init__(self, command_line):
        super().__init__(command_line)
        self.args = {}

    async def parse_arguments(self):
        if len(self.command_line.strip()) > 0:
            raise Exception("ps takes no command line arguments.")
        pass


class PsCommand(CommandBase):
    cmd = "ps"
    needs_admin = False
    help_cmd = "ps"
    description = "Get a brief process listing with basic information."
    version = 1
    is_exit = False
    is_file_browse = False
    is_process_list = True
    is_download_file = False
    is_upload_file = False
    is_remove_file = False
    author = "@djhohnstein"
    argument_class = PsArguments
    attackmapping = []
    browser_script = BrowserScript(script_name="ps", author="@djhohnstein")

    async def create_tasking(self, task: MythicTask) -> MythicTask:
        return task

    async def process_response(self, response: AgentResponse):
        pass