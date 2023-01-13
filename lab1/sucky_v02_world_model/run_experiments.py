from batch_simulator import run_agents_in_environment

#######################################
# Two options about what to do with the agent's log messages in absence 
# of a GUI pane
def log_to_console(msg):
    print(msg)

def log_null(msg):
    pass

########################################
    
dirt_density = 0.3
wall_density = 0.3
num_samples = 100
output_file_name = 'simulation_results.csv'
agents = [("agents/lab1agents.py",   "BestWorldModelAgent"),
           ("agents/lab1agents.py", "BestReactiveAgent"),
           #("agents/reactiveagent.py",  "NoSenseAgent"),
           ("agents/reactiveagent.py",   "SenseDirtAgent"),
           ("agents/worldmodelagent.py", "WorldModelAgent")
         ]
write_results_to_console = True


run_agents_in_environment(dirt_density, 
                          wall_density, 
                          agents, 
                          log_null, 
                          num_samples, 
                          output_file_name, 
                          write_results_to_console)
