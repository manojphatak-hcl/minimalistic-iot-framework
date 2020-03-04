# minimalistic-iot-framework

## The Problem
The demand for IoT / IIoT is very high & there are plenty of opportunities to push technologies to extent & create value. There is a need for application developers to be very agile, build a proof-of-concept very quickly, show it customers, work on the feedback & write production code.
Of course, they need some "platform" or "framework", so that they can just focus on writing the "business code".
While there is a plathora of IoT platforms like PTC's ThingWorkx, Amazon's AWS-IoT, Siemens' MindSphere and many others, there is a challenge to select a one that's appropriate for one. Most of these proprietory platforms are feature-rich, but they could be too sophisticated & heavy for building something quickly. While there are Open-Source platforms as well, each one has a different paradigm & there is a learning curve.

## Goal
Goal of this project to help a developer to select a platform for her need to start building the application, with modest learning curve.
Being "minimal", we have following parameters:
- Being Simple is more important than being Feature-Rich
- At the same, one should be able add features by plugging in the components
- Should have modest learning curve
- (Important) Should be Open Source
- Polygot: Should not restrict the application developer to use only one particular programming language
- Low Memory Footprint
- One should be able to run it in "containers"
- Should allow Horizontal Scaling
- Should allow backpressure

Its not very likely that we can get all these qualities in one single platform & there will be trade-offs. However, goal of the project is to make it easy for developers to understand the trade-offs.

## Development Values
- There are several sites that offer the comparison of IoT platform. But for us being "pragmatic" is more important than being "accurate"
- We will select a few "IoT Problem Statements" & implement the solution in multiple Open-Source Platforms
- Everything should be in the form of "Working Code".
- We may also end up writing our own platform, if we don't find a good minial one.

## Components
Any IoT platform would have following components / capabilities:
- Ability to Stream Data from constrainted device
- Message Broker for Asynchronous Communication
- Processors to process the strea in a Reactive Way
- Ability to build visualizations / dashboards
- Ability to plug-in Machine Learning component

## Problem Statements
Following are "candidates". Feel free to add more. We will need a range from "trivial" to "real world"
- Scraping data from the web
- PotHole Detection. 
  - Detect road conditions using mobile sensors, pictures
  - Feed it the processors & optionally a Machine Learning Model
  - Visualize it on Maps for Navigation
- [TODO] add more


## IoT Framework
Candidates:
- Node Red (https://nodered.org/)
- OpenIoT (http://www.openiot.eu/)
- ThingsBoard (https://thingsboard.io/)
