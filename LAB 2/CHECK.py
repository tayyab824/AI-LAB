"""Run: python lab2_check.py"""
from lab2_model import ThermostatAgent
from lab2_percepts import sample_percepts
import csv

def run_trace():
    agent=ThermostatAgent(); rows=[]
    print("STEP PREVIOUS   PERCEPT                  TARGET ACTION       SCENARIO")
    for i,p in enumerate(sample_percepts(),1):
        target,send,previous=agent.step(p)
        row={"step":i,"previous_mode":previous or "NONE","temperature_c":p["temperature"],"occupied":p["occupied"],"target_mode":target,"action":"SEND COMMAND" if send else "NO COMMAND","scenario":p["label"]}
        rows.append(row)
        print(f'{i:<4} {row["previous_mode"]:<10} {p["temperature"]:>3} C, {str(p["occupied"]):<5}       {target:<6} {row["action"]:<12} {p["label"]}')
    assert rows[0]["action"]=="SEND COMMAND"
    assert rows[1]["action"]=="NO COMMAND"
    assert rows[2]["target_mode"]=="OFF"
    assert rows[3]["target_mode"]=="HEAT"
    assert rows[4]["action"]=="NO COMMAND"
    assert rows[5]["target_mode"]=="OFF"
    assert rows[6]["target_mode"]=="OFF" and rows[6]["action"]=="NO COMMAND"
    with open("lab2_trace.csv","w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
    print("All assertions passed. Trace saved to lab2_trace.csv")
if __name__=="__main__": run_trace()
