class TraceLogger:

    def __init__(self):
        self.steps  = []

    def log_action(
            self, step, action
    ):
        self.steps.append(
            {
            "step" : step,
            "action" : action,
            "observation": None
            }
        )

    
    def log_observation(self, observation):
        self.steps[-1]["observation"] = observation

    def print_trace(self):

        print("\n")
        print("=" * 60)
        print("AGENT EXECUTION TRACE")
        print("=" * 60)

        for entry in self.steps:
            print(f"\nStep {entry['step']}")

            print("\nAction : ")
            print(entry["action"])

            print("\nObservation : ")
            print(entry["observation"])

        print("\n" + "=" * 60)
