﻿## DAY 3 - AFTER
# Setting the scene - this is in black
label office:

    scene bg black with Dissolve(2.0)
    play music reflective fadein 2.0 fadeout 1.0

    m "…"
    m "(Ugh.)"
    m "(The hell am I even waiting for?)"
    m "(The damage is already done.)"
    n "{i}* knocking sounds *{/i}"
    p "Who's there?"
    m "…It's me."
    p "Oh! Come on in."
    m "Okay."

    jump office_inside

# Inside the office
label office_inside:

    scene bg office with Dissolve(1.0)

    # Initial introduction and setting description
    n "The principal gestures to a stiff wooden chair on the opposite side of the desk."
    p "Have a seat! Make yourself comfortable."
    m "…Thanks."
    n "Masami eases himself into the chair. It feels about as uncomfortable as it looks."
    m "(I don't know what I expected.)"
    n "He shuffles around anyways, attempting to find the most bearable position he can."
    m "Sorry."
    n "The word comes out of his mouth on reflex. Masami flinches, startled. He turns away, face slightly flushed."
    m "I - "
    n "The principal chuckles."
    p "Don't worry, everyone's been complaining about it, not just you."
    p "Reminds me, I really need to go about replacing that chair..."
    m "…"
    n "Masami stares quietly at his fingers, which are interlaced and twitching in his lap."
    n "His simple apology from earlier blooms in his mind, large and looming, reducing the principal's voice into a background drone."
    m "(...It just slipped out.)"
    m "(Why did I say that?)"
    m "(It was just a chair.)"
    m "(She didn't even care about it.)"
    m "(What was I thinking?)"
    m "(What was I even supposed to be thinking?)"
    m "(Why do I still care about all the little things?)"
    m "(Why - )"

    jump office_question

label office_question:

    p "Masami?"
    n "Masami's head jolts back upright again."
    n "The principal's gaze on him is softer now and she leans back slightly, as if to appear less intimidating. More sympathetic."
    n "It doesn't make Masami feel any different, but he smiles a little and relaxes his tense shoulders as if it does."
    m "Yes?"
    p "I've baked some cookies, if you want any."
    m "Uh, I think I’m good."
    m "Thank you though."
    p "Are you sure? I've got plenty to spare."
    p "It's the least I can do for you."
    m "Yeah, I'm sure."
    m "(You know, it would be easier if you just cut the bullshit and said you don't want to be here on Christmas Eve either.)"
    n "The principal sighs."
    p "...I'll admit that this is a hard and unexpected conversation for me to have as well."
    p "Can you please stay with me?"
    n "Masami nods vacantly, staring straight ahead."
    p "The security camera near the breezeway recorded a student carrying out an act of vandalism near the carpool loop this past Sunday."
    p "It would have been a less…disruptive occurrence had the display not been so effectively crafted to provoke."
    m "…"
    n "Noticing Masami's reaction, the principal pauses for a moment."
    p "I mean to reassure you that we cannot say anything for sure from the footage alone."
    p "But, those of us who have reviewed it believe that the appearance and demeanor of the perpetrator strongly suggests it’s you."
    p "Do you…have anything you'd like to discuss with me about this?"

    # Choose how to respond
    menu:

        "Does it matter if it was me?":
            jump office_question_pa

        "What made you think so?":
            jump office_question_divert

        "(Continue to remain silent)":
            jump office_question_silence

# Masami answers passive aggressively
label office_question_pa:

    m "Does it matter if it was me?"
    n "The principal sighs again."
    p "I care about you just as I care about all my students."
    p "I want them to succeed and to not jeopardize their futures with the consequences of impulsive decisions."
    m "(Right. I’m sure you thought the same about {i}jie{/i}.)"

    jump office_outburst

# Masami diverts
label office_question_divert:

    m "What made you think so?"
    n "The principal smiles bitterly."
    p "For better or worse, we take on the traits of those around us."
    m "(Yeah, right. Just admit you never liked {i}jie{/i}.)"

    jump office_outburst

# Masami remains silent
label office_question_silence:

    m "…"
    m "(What do you want out of me? A confession?)"
    m "(As if that would change anything.)"

    jump office_outburst

label office_outburst:

    n "The principal leans forward slightly, her fingers laced."
    p "Masami, I've already been very lenient with you."
    p "Three days of suspension at the beginning of next semester is the least we can do for someone without a prior record."
    p "You are one of the best students in your grade, or in our school, even. Many of the underclassmen look up to you."
    p "Teachers consistently tell me how kind, how bright, how motivated you are. How promising of a future you have ahead of you."
    m "So they did."
    p "I am not trying to use this to dismiss the severity of our present circumstances."
    p "But they do make them all the more baffling."
    p "I want to understand where you're coming from, but you're not making this easy for me."
    m "…"
    p "I know that the past few days have been difficult for you."
    p "Losing a loved one isn't something to be taken lightly. It is necessary to take the time and space you need to grieve."
    p "Especially for someone like your sister, who was tragically gone so soon - "

    play music chaos

    m "Hmph."
    m "You don’t actually expect me to believe that, do you? That {i}jie{/i} actually amounted to anything in your eyes?"
    p "I did not say - "
    m "That's what you implied."
    n "Before he knows it, Masami has flown to his feet, hand planted on the desk in front of him."
    n "His voice remains quiet and steady, but the tone of it has sharpened."
    m "It's always been about the implications, hasn't it?"
    m "All the things that we want others to know, but won't dare speak into existence."
    n "The principal flinches."
    m "You don't deny it, do you?"
    p "Masami -"
    m "You said you wanted to understand me."
    m "Fine. I'll tell you then."
    p "…"
    m "All of us here are cowards."
    m "Fucking dancing puppets on strings."
    m "We're all pulling at each other because we're too damn stupid to know any other way to move."
    m "Get good grades to get into a good college. Get a good resume to get into a good job. Get a good salary to get a nice, big house you can retire in."
    m "Smile good enough that you won't feel like you need to roll over in your grave when you die."
    m "Feels good, doesn't it?"
    m "You know what happens the moment that someone decides they want to cut themselves free?"
    m "That they've had enough of the bullshit?"
    m "That they want to find out how to move on their own?"
    m "That they want - "

    stop music

    m "I - "
    m "..."

    play music emotional fadein 2.0

    n "Suddenly, just as it begins to crescendo, Masami's voice breaks and the dark fire in his eyes flickers out. Hollow."
    n "His gaze drops back to the desk again, but he remains standing."
    m "(Shit.)"
    m "(I'm doing it again.)"
    m "(Taking things out on people who just want to help.)"
    m "(Repeating {i}jie’s{/i} mistakes all over.)"
    n "He inhales quietly."
    p "Masami?"
    m "…Never mind."
    p "…"
    p "I'm sorry. I didn't mean to bring up things like this for you."
    m "…"
    m "It shouldn't matter. I…"
    m "I'm fine."
    p "…"
    m "…"
    m "Three days, right?"
    p "A three day suspension, yes."
    m "…I'll be back after three days, then."
    p "Alright. Please, take care of yourself, Masami."
    m "…"

    jump car

# Masami heads to his car
label car:

    scene bg black with Dissolve(1.5)
    scene carday with Dissolve(1.5)

    n "Masami heads out of the office and back to his car."
    n "Once he's inside, he leans against the headrest and sighs."
    m "(I've really been a loose cannon lately, haven't I?)"
    m "(I don’t know if I even believe half of what I said. But some days, things like that feel awfully real.)"
    n "Masami's gaze instinctively drifts towards a magpie keychain hanging from his car keys. He catches himself and looks away."
    m "…"
    n "He sits quietly there for a couple more minutes before he starts up the engine for the drive home."
    n "When he hits the open road, the speakerphone rings in with an incoming call."
    m "(Oh. It's Mom.)"

    # Decide whether or not to pick up
    menu:

        "Pick up":
            jump phone_mom

        "Ignore":
            m "(I don't feel like answering her right now.)"
            m "(She probably just wants to know what time I'll get back.)"
            m "(She'll understand.)"
            m "…"

            jump masami_home3

# Masami's mom calls him
label phone_mom:

    n "Masami presses the button on the steering wheel to answer, letting a lilting, slightly accented voice drift in through the speakers."
    m "{i}Wei{/i}? {i}Ma.{/i} I'm done."
    mm "What did - "
    m "Three days."
    mm "…Masami - "
    m "It's alright. I don't care."
    mm "…Okay."
    n "Masami blinks."
    m "Okay?"
    mm "Okay."
    m "That's it?"
    mm "Yes."
    m "…"
    m "I thought…"
    m "Never mind."
    n "Masami sighs."
    n "The other end of the line goes quiet as well, dropping down into a mix of static and light chattering."
    n "Masami listens in for a bit, trying to pick out the individual voices in the background, but everything just blurs together."
    m "Is everyone already there?"
    mm "Yes. We are waiting for you. All four of your friends here too."
    m "…"
    m "I'll be there in ten."
    mm "Okay."
    mm "Love you."
    m "…"
    m "Love you too."
    n "Masami hangs up the phone and continues to drive in silence."

    jump masami_home3

# Masami arrives at his house and thinks about some things
label masami_home3:

    n "Some time later, Masami pulls up to his street."
    m "(The driveway is already full. The curb, too, for a couple blocks.)"
    n "Sighing, Masami circles around and goes to park at the nearest spot down the road."
    m "(I…didn't expect so many people to be there.)"
    m "(Funny how everyone talks about {i}jie{/i} now. But only because she's actually gone.)"
    n "Masami shuts his eyes."
    n "When he opens them, he finds himself staring at the magpie keychain again."
    m "(I guess I've sort of known all along that it would end like this.)"
    m "(...Whatever.)"
    n "He musters what remained of his willpower and takes his keys out from the ignition."
    n "Cradling the magpie delicately in his hands, he cracks open the car and steps outside."
    m "(If I keep waiting until I'm ready, I'll never leave.)"

    stop music fadeout 2.0
    scene bg black with Dissolve(2.0)

    jump class_3
