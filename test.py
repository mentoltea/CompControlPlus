import command

import basic_commands
import state_commands
import cmd_commands

state_commands.state.state.anewattr = 1  # pyright: ignore[reportAttributeAccessIssue]
print(state_commands.state.state.__dict__)

query = '/reset! YES'
res = command.evaluate_blocks(command.parse_query_to_blocks(query))
print(res.get())

print(state_commands.state.state.__dict__)