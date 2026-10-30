# Stakeholder Interview: Construction Management Expert

- **Date:** Thursday, October 29, 2026, 9:00 to 9:20 am (Google Meet)
- **Interviewee:** Construction Management Expert
- **Interviewer:** GC Team 7, INFO 492
- **How this was made:** recorded as a phone voice memo, auto-transcribed, then cleaned for readability. Filler words and false starts are removed, mis-transcriptions are corrected (Andersen, Haggett Hall, Kirk Hochstatter, UW), and unclear audio is marked [unclear]. The recording starts shortly after the call began. Conversation after the call ended is not included.
- **Permission:** Public sharing of this interview transcript is pending confirmation. Do not upload to a public repository until permission is confirmed.
## Summary

1. **Where RFIs lose time:** mostly in the formal review chain (sub-tier sub, sub, GC, owner, architect, engineer). An RFI needing a 2-day answer can spend a day and a half in the chain before reaching the expert. She doubts AI can remove that chain.
2. **A workaround teams use:** sending an informal early copy (a "bootleg PDF") straight to the engineer so review starts while the formal RFI moves. Some teams resist this because RFIs are legal documents, and subs act at their own risk without formal direction.
3. **Due dates as ground truth:** a "good working assumption," because GCs set due dates against the construction schedule. Items with schedule float may get looser dates.
4. **Alarm fatigue:** flags are only useful if they match what's being built now. High stakes (a seismic question) isn't the same as urgent if the work is weeks away. She suggested tying each flag to a schedule activity and giving the design manager a weekly priority list.
5. **Credibility and next steps:** test the prototype with potential users in scenario-based mock interviews. Referrals: Kirk Hochstatter (UW CM, 20+ years in industry, lean construction, PhD), UW CM seniors who managed RFIs as interns, and possibly a design-manager contact.

## Transcript

**Interviewer:** [Recording starts mid-introduction.] ...on our project: we're UW Informatics. Oh, and this is my teammate, who will be joining in for the meeting. For a little bit of context on what we're working with: we're a four-person Informatics team in the INFO 492 class. The theme for this quarter is construction informatics, and specifically we're looking at the RFI cycle. When a contractor hits a question the drawings don't answer, it goes to the design team, and that work can stall until the answer comes back.


What our team is doing is testing whether an AI agent can help general contractors triage RFIs as they come in. We're looking at a system that can tag why each RFI was raised, who should answer it, its level of urgency, and whether it follows up on an earlier RFI. A person always reviews everything, and the agent never answers the RFI itself. There's always a human in the loop.

Our thesis is that with better triage, mainly by flagging urgent RFIs earlier, we can cut RFI processing time by about 10%. We spoke to Andersen, and they shared the real RFI log from the UW Haggett Hall project. That gave us 35 construction-phase RFIs from, I believe, early 2025, with the dates each was created, when it was due, and the responses. Does all of that check out? I know the project file we shared is probably a little dense. Does that help for context?

**Interviewee:** Yeah. Yeah, for sure.

**Interviewer:** Awesome. [Brief audio echo.] For what we found: from the log itself, RFIs on that project stayed open for a median of about 6 days, and of the 35 we were given, 11 closed late. The ones Andersen gave only 2 to 4 days were late 7 out of 12 times, and they stayed open as long as everything else. So even when the priority was higher, "we need this back in 2 to 4 days," they were late and stayed open as long as everything else. Priority didn't really change how fast the information came back.

With our agent, we picked the correct responder and caught follow-ups every single time. Every time an RFI referenced a previous one, we identified that. But for urgency, we got it right only 4 out of 10 times, which is worse than a simple keyword rule. It tends to treat high stakes as urgent.

So our open question is: is urgency a triage problem that a tool can fix, or is the delay somewhere a tool can't reach? We have a couple of questions prepared, if you'd be willing to answer them or just give your input.

**Interviewee:** Sure, I'll try.

**Interviewer:** Okay, awesome. I looked a little into your research on how design and construction teams communicate. Where does an RFI usually lose time? Is it recognizing that it's urgent, getting it to the right person, or the response from the design team?

**Interviewee:** Probably all of the above, I would think. There are the formal channels it has to go through. Say there's a lower-tier subcontractor, a third-tier sub. Everyone in the chain has to review it along the way. If I'm a piping subcontractor, it goes to my mechanical subcontractor, and they review it. It goes to the general contractor, and they review it. It goes to the owner, and they review it. It goes to the designer, and they review it. It goes to the mechanical engineer to finally answer it. That's part of the process that may take time, and I don't know if AI can solve that problem, because there is this review process.

One of the ways one of our teams solved it was what they called a "bootleg PDF." They sent it directly to the engineer to start the review while the formal chain was going through. Then, once the engineer got the formal RFI, they'd already reviewed it; they just confirmed it was the same thing. The team had enough trust that they sent an informal response, verbally, saying, "Yes, go buy that piece of equipment," and then the formal response came through the formal channels. So that's the example we have from the research.

Can you hear me okay? I'm in kind of a noisy spot.

**Interviewer:** Oh, no, perfectly clear. I don't hear anything.

**Interviewee:** Okay, good. Filters, they're great.

**Interviewer:** Yeah, I know, right? So it's almost escalating the issue informally, knowing it has to trickle through all those teams, and getting it to the person who will eventually have the most weight in actually completing that particular thing.

**Interviewee:** Yeah, because it has to get to the person who has the expertise to respond. You could even make a flowchart with the engineer over here on the design side, then the architect, the owner, the general contractor, the subcontractor. That chain of command can be a long part of the process. If an RFI needs a two-day response, it could spend a day and a half in the chain before it gets to the person.

So perhaps there's a way to flag it for early review while it's still getting approved, if they're on a centralized management system. If the team could say "early review," then when it gets approved for review, you're already responding. Something like that. I don't know if teams would be up for formalizing that informal chain.

**Interviewer:** Yeah. What our agent is currently really good at is figuring out who is most responsible for a particular RFI, like you said. So, based on what you're saying, I'm thinking of using that same identification to bring the RFI to them informally, while also helping it move through the whole flow you described.

**Interviewee:** Yeah, yeah. There may be some teams and some people who push back on that informal exchange, because they're concerned about anything informal. They want the formal chain, because documents are so tied to the legal structures of the industry. So there may be some pushback. But for some of the teams we worked with, that's how they got through the delay: facilitating that preliminary review early. You could call it an early preview or a preliminary review, something less legal than the formal approval.

**Interviewer:** And to clarify: even if that group or person reviewed the RFI most relevant to their work, they couldn't act on it until the entire formal process is complete? If it were an adjustment to the building, they couldn't do any of that until then?

**Interviewee:** But they'd know. Well, right. [She crosses a street.] If they were to do something, it would be at their own risk. The subcontractor protects themselves by following the directions they're given by the designers and the general contractor. If they do anything before they get formal direction, it's at their own risk to redo it if it doesn't align with the formal direction. That's where their risk lies, so some contractors won't do anything until they have direction.

But then you get into the problem where, often in the structural phase of a project, they're pouring concrete. The concrete schedule doesn't move and doesn't wait for anybody. Say they're not getting the response they need on certain locations, on blockouts, as they're called, where they block out the concrete so there's room for a duct or a pipe to go through the wall or the slab. If that information doesn't arrive, what do they do? The concrete's getting poured. They have to make a choice. That's part of the RFI challenge: getting everybody the information they need to keep up with the pace of construction. [unclear] I don't think that particular detail matters, but if they don't get the blockout in place, they might have to spend time jackhammering the concrete out to make the hole they need. So it's an expensive delay.

**Interviewer:** Okay. Another thing: in our work, we used the contractor's own due dates as our ground truth for urgency. Whatever they wrote down as the urgency, that's what we used. From your experience on real projects, do those due dates reflect actual urgency, or are they defaults, contract defaults, habit, or something else?

**Interviewee:** I think they would reflect urgency, because they're aligning those due dates with the construction schedule. Like I said, if they have a concrete floor coming up and need these answers to prepare for it, they'll align the due dates with that. But if it's a landscaping question, or something external to the building, something with what construction scheduling calls float, wiggle room on the schedule so they can do it later without much impact, those might have more flexible dates. I don't know whether that flexibility shows up in the due date, but due dates tend to be driven by the construction schedule's requirements.

**Interviewer:** Okay, yeah. That was basically the ground truth we compared against, so we were wondering whether it's a good baseline to use. Thank you.

**Interviewee:** Yeah, I think that's a good assumption. That's a good working assumption, for sure.

**Interviewer:** Awesome. Just two more questions. Our agent is very consistent in its responses, but it over-flags urgency. I saw you've worked with tools like BIM. For people in industry, what makes a team trust a tool's flags, and what makes them start to ignore it? Human factors like trust, and alarm fatigue, which we think our tool could definitely cause.

**Interviewee:** Yeah, in construction you're going to see a lot of alarm fatigue, because there's always something under pressure. In construction the mentality is a little different, because it's about the job site and the physical production. For the people in the field managing that work, it's all about keeping the job site moving forward: getting materials, people, and equipment where they need to be, and the information they need to do the construction. So it's not necessarily about alarms; they're lining everything up to make that happen.

If the alarms were helping them bring forward time-sensitive things, that would be useful. If they're alarming on things that aren't important, they'd get fatigued, because they'd think, "Now I can't trust whether this alarm is needed, or whether it's a false alarm that isn't addressing what's happening on the job site this week." So I can imagine people wouldn't find a tool useful if it gives alarms about things that aren't relevant to what they're currently working on. Say they're pouring concrete on level two and they get an alarm about something on level four. They'd say, "I'm not working on level four right now. We'll need that information in two weeks, but we don't need it right now."

The designers are in a different situation. They do want to support construction, but they're hired to do the design, so in the immediacy of their work they don't have the same pressure, because they're not managing the job site. In a way, they're done with the bulk of their work: they made the design and shipped it off to construction. Now, on Haggett Hall the designers are more integrated. They're on the job site with the builders, so they share more of that sense of urgency.

A tool for that design manager who's on site with the contractor could give them a list of priorities: "These things must happen this week, because they're being built." That gives them a priority list for getting answers back to the team. Then, "These next things need answers by next week, and these by two weeks out." That helps the design manager manage the responses and perhaps be more proactive. But if it were jumbled, or they got alarms that didn't help with that prioritization and just raised something to a higher priority because it's important, say it really affects the seismic structure, but you don't need that answer for construction for two or three weeks, then it's not helping them get the most urgent RFIs answered.

**Interviewer:** So what I'm hearing is aligning these alerts with the timeline of the actual construction.

**Interviewee:** Yeah, that's helpful. It would be very cool to integrate the construction schedule with the alarms, to say, "This alarm connects to this activity happening on this date." I think that would help the whole team understand the urgency.

**Interviewer:** Okay. Again, we have 35 RFIs we're looking at, and we're asking for more. For a project like this, what would make our evaluation or testing credible to construction researchers? What does it take to say we've analyzed real data, built something with it, and it holds water?

**Interviewee:** From a research methods standpoint?

**Interviewer:** Yeah, from a research or data quality perspective, or what factors to include in our project, something like that.

**Interviewee:** That's a good question. Because you have a prototype, one method at your disposal is user testing with that prototype: interviews with potential users. My lab did that this summer with another tool. You develop interviews with potential users and a mock-up where they actually go through a scenario and use the tool in that scenario, and then they answer reflective questions on whether they find the tool useful or not. I don't know that you have the opportunity to deploy a pilot in a real project context. If you can't get to a real project context, you could do a mock trial in an interview setting.

**Interviewer:** That lines up perfectly with my next question. Would you be able to point us to someone at UW, through your lab connections or students, maybe a practitioner, a former student, or someone in your lab who works with RFIs and really understands what that looks like in industry, who might talk with us this week or in the future? Maybe an interview like you described, or stakeholder feedback like this. We're happy to set up an intro, explain the site, or whatever helps.

**Interviewee:** Yeah, yeah, I'm happy to. My first recommendation might be Kirk Hochstatter. He's adjunct faculty in our department; actually, I think his title is assistant teaching professor. He's been in the industry for 20-odd years and is also very interested in lean construction, the area of practice that looks at making the job site much more efficient. He might be a nice one. I don't know if he's available this week. He also has a PhD, so he appreciates both research and practice. So I [unclear: likely "can introduce"] you to Kirk.

Honestly, almost every senior in our program just managed RFIs this summer; that's one of the things they do as interns. So you could probably grab any senior in our program, and they'd be a good trial for you. They're pretty busy, but if you put together a brief introduction of what you're looking for, we could distribute it to the seniors and see if anybody's interested. Peer to peer might be kind of fun.

**Interviewer:** Yeah, for sure.

**Interviewee:** And then, thinking specifically about RFI management... I'm happy to. You have the contacts at Andersen and Haggett Hall, right?

**Interviewer:** Yes, yes, we're working on them. We've learned that students asking about RFI handling can sometimes be a little tricky, because they don't know what information to give. So if we can find people with general industry experience or academic experience, that would be great. Thank you so much.

**Interviewee:** Yeah, I think it would be good for you to connect with a design manager, because the construction manager is the one receiving these RFIs and trying to get them answered, and one piece of your work is understanding the design side. Kirk might be able to recommend some design partners, and I could see if one of my contacts would be available too. I'm thinking about who might be available while I'm walking here. I could try to reach out to someone.

**Interviewer:** Awesome, thank you.

**Interviewee:** So, happy to follow up. If you could send a brief introduction of what you're looking for, an invitation, I can share it. Do you want me to share it with the seniors?

**Interviewer:** If that's something you could do, that would be great. We'd really appreciate it. On my end, I'll send over that brief intro blurb with all the context and some of the project details. Thank you so much for offering to connect us with more people.

**Interviewee:** Yeah, yeah. When I was talking to your professor about this project, I recommended that you connect with the senior class. I thought it would be fun to see the student experience, because they've just come off internships where many of them managed RFIs for their companies, and maybe for owners. I think they'd have fresh insight into what it feels like to manage RFIs across a lot of different kinds of projects. You may get overwhelmed by information, but that's better than none: 90 people with different experiences.

**Interviewer:** I bet. Awesome. Thank you so much for your time, especially on such short notice. We needed some grounding for our project before our presentation tomorrow, so this was very helpful. I'll send over my part, and if you have any other questions for me, feel free to reach out. Thank you so much.

**Interviewee:** Yeah, yeah. Good work, and I look forward to hearing how it goes.

**Interviewer:** All right, take care. Have the rest of your day.

**Interviewee:** Thank you. Bye.

[End of interview.]
