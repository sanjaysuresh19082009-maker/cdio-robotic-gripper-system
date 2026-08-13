# 🤖 CDIO Automated Cube Pick-and-Transfer System

[cite_start]An automated pick-and-place robotics system built using the **CDIO** (Conceive – Design – Implement – Operate) engineering framework[cite: 27]. [cite_start]The system integrates two educational off-the-shelf kits—the **Klaw MK2 Robotic Gripper** [cite: 30] [cite_start]and the **Kitronik Linear Actuator** [cite: 31][cite_start]—and custom 3D-printed parts [cite: 68][cite_start], all controlled by a **BBC micro:bit** microcontroller[cite: 32].

---

## 🛠 Project Overview & Architecture

* [cite_start]**Role:** Programming Lead 1 (Software Design, MicroController Logic, Servo Drivers & Integration) 
* [cite_start]**Controller:** BBC micro:bit v2 [cite: 35, 75]
* [cite_start]**Actuators:** 2x Servos (1 for Gripper, 1 for Linear Actuator Carriage) [cite: 66, 154]
* [cite_start]**Inputs/Outputs:** External Start Button [cite: 73, 177][cite_start], Integrated Speaker (Audio Feedback) [cite: 33, 76]



### System Component Stack:
1. **3D-Printed Actuator Base:** Anchors the assembly to the workspace[cite: 84, 99].
2. **Kitronik Linear Actuator Kit:** Translates rotational servo motion into linear carriage movement[cite: 85, 165].
3. **3D-Printed Gripper Adaptor:** Serves as a custom mounting bracket between the linear carriage and the claw assembly[cite: 86, 104].
4. **Klaw MK2 Robotic Gripper:** Serves as the end-effector to grip and hold the target object (cube)[cite: 87, 162].

---

## 📂 Repository Structure
├── main.py        # Main execution script running the state machine & sequence logic
├── servo.py       # Custom helper library for MicroPython PWM servo angle control
└── README.md      # Documentation
