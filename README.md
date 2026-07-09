# 💧 AquaAssess

## Rooftop Rainwater Harvesting & Artificial Recharge Potential Assessment System

**AquaAssess** is a web-based application developed for the **on-spot assessment of Rooftop Rainwater Harvesting (RTRWH) and Artificial Recharge (AR) potential**.

The system helps users and field officers estimate the amount of rainwater that can be harvested from a rooftop using site-specific parameters such as **rooftop area, annual rainfall, runoff coefficient, and roof construction type**.

The application combines **real-time assessment, interactive process visualization, runoff analysis, rainfall insights, educational content, and digital assessment storage** in a single platform.

---

## 📌 Project Overview

Water scarcity and groundwater depletion are major environmental challenges. Even in regions receiving significant rainfall, a large quantity of rooftop runoff is often lost through drainage systems without being effectively harvested or used for groundwater recharge.

Traditional rooftop rainwater harvesting assessments may require manual data collection and separate calculations, making the process time-consuming and difficult to maintain for multiple sites.

**AquaAssess** provides a digital solution that allows users to enter site-specific parameters and instantly estimate rooftop rainwater harvesting potential.

The project supports:

* Rapid field-level assessment
* Rooftop runoff estimation
* Real-time harvestable water calculation
* Runoff coefficient analysis
* Rainfall distribution insights
* Understanding of rainwater harvesting processes
* Awareness of artificial groundwater recharge methods
* Digital storage of assessment records

---

## 💡 Why This Project?

Consider a building with a large rooftop located in an area receiving significant annual rainfall.

During rainfall, water falls on the rooftop and flows through gutters and drainage systems. Without a proper harvesting system, much of this rooftop runoff may be lost.

At the same time, the same region may experience:

* Seasonal water shortages
* Increasing groundwater dependency
* Declining groundwater availability
* Limited awareness of rooftop harvesting potential

This creates an important question:

> **How much rainwater can potentially be harvested from a particular rooftop?**

AquaAssess helps answer this question by converting measurable site parameters into meaningful rainwater harvesting estimates.

---

## 🎯 Project Objectives

The main objectives of AquaAssess are:

* To develop a web-based platform for on-spot rooftop rainwater harvesting assessment
* To estimate annual harvestable rooftop runoff
* To use site-specific rooftop area and rainfall data
* To incorporate runoff coefficient into the estimation process
* To support different roof construction types
* To provide real-time calculation results
* To visually explain the complete rainwater harvesting workflow
* To provide educational information about rainwater harvesting and artificial recharge
* To digitally store assessment information for future reference

---

## ✨ Key Features

* 💧 On-Spot Rooftop Assessment
* ⚡ Real-Time Calculation Preview
* 🏠 Multiple Roof Construction Types
* 📊 Runoff Coefficient Analysis
* 🌧️ Rainfall Distribution Insights
* 🎞️ Animated Rainwater Harvesting Process
* 📚 Interactive Knowledge Base
* 💾 Assessment Record Storage
* 📱 Responsive Web Interface
* 🌱 Artificial Recharge Awareness

---

# 🧩 Project Modules

## 1. 🌧️ Rainwater Harvesting Process Visualization

This module visually demonstrates the complete rooftop rainwater harvesting process through an interactive animated interface.

The process includes:

1. **Rainfall** – Rainfall acts as the primary water source.
2. **Rooftop Collection** – Rainwater falling on the rooftop is collected as runoff.
3. **Conveyance** – Gutters and downpipes transport collected water.
4. **First Flush** – Initial contaminated runoff can be diverted.
5. **Filtration** – Water passes through suitable filter media.
6. **Storage** – Filtered water can be stored in tanks, cisterns, or sumps.
7. **Groundwater Recharge** – Surplus water can be directed toward suitable recharge structures.

---

## 2. 📊 Component Analysis Module

This module provides visual insights into important parameters affecting rooftop rainwater harvesting.

### Runoff Coefficient Analysis

The AquaAssess model represents indicative runoff coefficients for different roof surfaces:

| Roof Type              | Runoff Coefficient |
| ---------------------- | -----------------: |
| Metal / GI Sheet Roof  |               0.90 |
| Concrete / RCC Roof    |               0.85 |
| Asbestos Sheet Roof    |               0.80 |
| Tiled / Mangalore Roof |               0.75 |
| Thatched Roof          |               0.60 |

> **Note:** Actual runoff coefficients may vary depending on roof condition, slope, rainfall characteristics, maintenance, and local conditions.

### Rainfall Distribution Insights

The application provides a visual comparison of rainfall variation across selected Indian regions, helping users understand how geographic rainfall differences affect harvesting potential.

---

## 3. 📚 Knowledge Base Module

The Knowledge Base provides educational information about:

* Introduction to Rainwater Harvesting
* Types of Rainwater Harvesting Systems
* Harvesting Potential Calculations
* Artificial Groundwater Recharge
* Related Government Policies and Schemes

The module helps users understand both the theoretical and practical concepts behind rainwater harvesting.

---

## 4. 📝 Site Assessment Module

The Site Assessment Module is the main functional module of AquaAssess.

The user enters:

* Field Officer / Applicant Name
* Site Location
* Rooftop Area in m²
* Annual Rainfall in mm/year
* Runoff Coefficient
* Roof Construction Type

The current assessment interface supports:

* Concrete Roof
* Tiled Roof
* Metal Roof

---

## 5. ⚡ Real-Time Calculation Module

As the user enters the assessment parameters, AquaAssess performs real-time calculations.

The system displays:

* Estimated Harvestable Volume in m³/year
* Estimated Total Litres per Year
* Average Annual Yield Equivalent per Day

This allows users to immediately observe how rooftop area, rainfall, and runoff coefficient affect the estimated harvesting potential.

---

## 6. 💾 Assessment Storage Module

After entering and reviewing the site information, the user can select:

**Calculate & Save Assessment**

The assessment data can then be stored through the application backend for future reference and analysis.

---

# 📐 Core Calculation Formula

The project estimates annual rooftop rainwater harvesting potential using:

```text
V = (A × R × C) / 1000
```

Where:

```text
V = Estimated Annual Harvestable Volume (m³/year)

A = Effective Rooftop Catchment Area (m²)

R = Annual Rainfall Depth (mm/year)

C = Runoff Coefficient
```

The division by `1000` converts the result into cubic metres.

---

## 🧮 Example Calculation

Assume:

```text
Rooftop Area = 150 m²
Annual Rainfall = 800 mm/year
Runoff Coefficient = 0.85
```

Calculation:

```text
V = (150 × 800 × 0.85) / 1000

V = 102 m³/year
```

Therefore:

```text
Estimated Annual Harvestable Volume
= 102 m³/year

Total Water
= 102,000 litres/year

Average Annual Daily Equivalent
≈ 279 litres/day
```

> **Note:** Actual water availability may vary depending on rainfall distribution, first-flush diversion, filtration losses, storage capacity, overflow, and maintenance conditions.

---

# 🔄 Project Workflow

```text
User Opens AquaAssess
        ↓
Explores Rainwater Harvesting Process
        ↓
Reviews Runoff and Rainfall Insights
        ↓
Accesses Knowledge Base
        ↓
Opens Site Assessment Form
        ↓
Enters Applicant / Field Officer Details
        ↓
Enters Site Location
        ↓
Enters Rooftop Area
        ↓
Enters Annual Rainfall
        ↓
Selects Runoff Coefficient
        ↓
Selects Roof Construction Type
        ↓
System Performs Real-Time Calculation
        ↓
Displays Harvestable Volume
        ↓
Displays Total Litres per Year
        ↓
Displays Average Daily Equivalent
        ↓
User Submits Assessment
        ↓
Assessment Data is Saved
```

---

# 🛠️ Technologies Used

### Frontend

* HTML5
* CSS3
* JavaScript
* HTML Canvas API

### Backend

* Python
* Flask

### Database

* PostgreSQL

### Development Tools

* Visual Studio Code
* pgAdmin
* Git
* GitHub

---

# 🎥 Project Explanation & Demonstration Video

A complete project video explaining:

* Self Introduction
* Project Introduction
* Reason for Choosing the Project
* Real-Life Problem Scenario
* Project Domain
* Working Methodology
* Rainwater Harvesting Process
* Project Modules
* Site Assessment
* Real-Time Calculation
* Final Project Outcome

is available below.

## ▶️ Watch Project Demo

**Google Drive Video Link:**

(https://drive.google.com/file/d/1jKfg_OBCYm-9tX2S8J30TCJXBqkOtuYl/view?usp=drivesdk)
---

# 🌱 Project Benefits

* Supports rapid rooftop assessment
* Reduces repetitive manual calculations
* Provides immediate estimation results
* Improves understanding of rooftop runoff potential
* Supports digital assessment record maintenance
* Promotes rainwater harvesting awareness
* Promotes artificial recharge awareness
* Supports sustainable water management planning

---

# 👥 Intended Users

* Field Officers
* Engineers
* Researchers
* Students
* Educational Institutions
* Homeowners
* Local Authorities
* Water Resource Planning Teams

---

# 🔮 Future Enhancements

Future versions of AquaAssess can include:

* Automatic rainfall data retrieval
* GPS-based site identification
* GIS map integration
* Automated rooftop area estimation
* Soil and infiltration parameter integration
* Groundwater depth integration
* Site-specific recharge structure recommendation
* Engineering sizing of recharge structures
* PDF assessment report generation
* Assessment history dashboard
* Mobile application support

---

# 👨‍💻 Developer

**ARYA R**

B.E. Computer Science and Engineering
Specialization in Artificial Intelligence & Machine Learning

**VSB Engineering College**

---

# 📄 Disclaimer

The calculated results are estimates based on the input parameters provided by the user.

Actual rainwater harvesting performance may vary depending on:

* Local rainfall distribution
* Roof condition
* Roof slope
* First-flush diversion
* Conveyance losses
* Filter performance
* Storage capacity
* Overflow
* Maintenance practices
* Local site conditions

---

# 📄 License

This project is developed for academic, educational, and research purposes.

---

⭐ **If you find AquaAssess useful, consider giving this repository a star.**
