﻿## DAY 1 - BEFORE
label class_1:

    scene bg hallway with Dissolve(1.0)
    play music lighthearted fadein 1.0

    # SEFF: SCHOOL BELL RING
    m "Thanks, Mr. Friedman! Happy holidays to you, too!"
    n "Masami waves goodbye to his physics teacher before he steps out of the classroom, joining the sea of students heading to lunch."
    m "(Phew. I can't believe that - )"
    n "Suddenly, his phone buzzes in his pocket."
    m "(Hm. It's probably Sabie again. I wonder what she's up to this time.)"

    jump phone_1a

# Glitch ON
label phone_1a:

    stop music fadeout 1.0
    play music chaos

    call phone_open(True)
    call message(s, "Hey dumbass. I know who you really are. It'd be a shame if I told everyone, wouldn't it? ;)", True)
    call phone_close()

    jump class_1_panik

# Glitch OFF, cuts back to Masami
label class_1_panik:

    n "Masami nearly drops his phone."
    m "What the hell?"
    n "He nervously picks up his phone again."

    jump phone_1b

# The previous message disappears from the screen revealing the actual message:
label phone_1b:

    stop music fadeout 1.0

    call phone_open(True)

    call message(s, "dude", True)
    call message(s, "rohan is bullying me again")
    call message(s, "send help :(")

    call phone_close()

    jump class_1_kalm

# Cuts back to Masami
label class_1_kalm:

    play music lighthearted fadein 1.0

    n "Masami exhales slowly and slides the phone back into his pocket."
    m "(It's okay. I'm just seeing things.)"
    n "He rubs his temples."
    m "(Dammit. I should have gotten back earlier last night. Three hours is definitely not enough sleep.)"
    m "..."
    m "(I'll just reply to Sabie in person.)"

    jump lunch_1a

# Back to lunch
label lunch_1a:

    stop music fadeout 1.0
    scene bg black with Dissolve(1.0)
    scene bg courtyard with Dissolve(1.0)
    play music uptempo fadein 1.0

    n "As per usual, Masami hears the chaos long before he sees it."
    m "Well. Here we go again. Might as well try to end this one before it starts."

    show rohan annoyed at right
    show sabie annoyed at left
    with Dissolve(0.1)

    n "He hurries in as quickly as he can to find Rohan and Sabie engaged in another one of their tabletop battles."
    r "Hey, let go of my phone!"
    s "But you gotta delete those videos you took of me last night."
    r "What? No! They were good videos."
    r sad "Besides I - I wasn't even planning on sharing them."
    s "I don't trust you. You sent those drunk karaoke videos last time without a second thought."
    r annoyed "But Smash videos are different!"
    s "No, they are not."
    r sad "Why?"
    s worried "Ugh, spare me, will you? The number of times I suicided with Kirby was - "

    show sabie surprised

    n "Suddenly she freezes when she catches sight of Masami."

    stop music fadeout 1.0

    s mischievous "Oh. Hey. Look who it is."

    # Depending on if you supported Sabie on the third day
    # GLITCH ON

    play music chaos fadein 1.0

    hide rohan with Dissolve(1.0) # TODO: Fix animation such that Sabie dominates or something else disturbing happens!

    if support == "Sabie":

        s "Feel like coming to help me again?"
        s "Or are you going to leave me out to dry like you did to Alyssa because you've got commitment issues?"
        s "I should hope that a good old family friend means something to you, {i}ge{/i}."
        s happy "But then again, Xinyi did decide to leave her poor little brother behind."
        s "Who knows how much more you've learned from her? You two were close after all."

    else:

        s "Are you going to help me this time?"
        s "Or are going to leave me to suffer alone."
        s "I wonder if it's worth it for me to care about someone who didn't care for me back."
        s happy "That's what Xinyi did to you, after all."
        s "It's only fair that you take it out on the rest of us, right {i}ge{/i}?"

    m "W-What? When did I ever think that?"

    # Glitch OFF
    stop music fadeout 1.0
    show rohan sad at right
    play music uptempo fadein 2.0

    s worried "Uh…I guess you could start thinking about helping me right about now. Kinda in a tough spot, as you can see."
    m "Ah."
    n "Masami swallows."
    m "Rohan, maybe this time if you - "
    r "Does it matter what I do?"
    stop music fadeout 1.0

    # Glitch ON

    play music chaos fadein 1.0

    hide sabie with Dissolve(1.0) # TODO: Similar fix as before!

    r annoyed "I’ll answer that question for you. No, it doesn't."
    r "You're the only one here that she'll even listen to and you know that."
    if support == "Rohan":

        r "Stand up for me like you did last time."
        r sad "Or do I not matter to you either?"

    else:

        r sad "But definitely, go ahead. Let her walk all over to me."
        r "I won't care."

    m "N-No! It's not like that. I care about you guys, I promise."
    # Glitch OFF

    stop music fadeout 1.0
    show sabie worried at left
    show rohan neutral at right
    play music uptempo fadein 2.0

    n "Sabie and Rohan exchange glances. The phone hangs between them in their limp grasps, forgotten. "
    r "Uh, we already knew that part, but thanks."
    s "Is there something that you're thinking too hard about, {i}ge{/i}?"
    m "I - "
    n "Masami runs his hand through his hair."
    m "It's nothing. Just tired. You know what happens when you don't get those eight hours."
    n "Sabie and Rohan just stare at him."
    m "(Shit. I should have known they wouldn't buy it. Not when they've got a worse sleep schedule than me.)"

    show tyree
    hide sabie
    hide rohan

    t "Ah."
    n "Masami jumps."
    m "Wait, when did you - "
    n "His eyes land on Tyree's usual spot where he is indeed sitting and eating his salad."
    t "Same time as always."
    m "Oh."
    m "Sorry, I am really out of it today."

    stop music fadeout 1.0

    t "Hm."

    # Glitch ON

    play music chaos fadein 1.0

    t happy "There is no use trying to destroy who you once were."
    if support == "Tyree":

        t "You may be able to ignore others for a short while, but you cannot ignore them forever."
        t "Not if you've expressed affection for them before. It will be too late then."
        t neutral "They will always want the old you back. As they should."
        t worried "What will they say when you cannot return to them?"

    else:

        t "People will always expect the same good thing out of you once you've given it to them before."
        t "They will accept no less and we must follow through."
        t neutral "This is how we become who we need to be."
        t worried "Is it too much to ask for, to make a wise decision more than once?"

    hide tyree

    n "Masami backs up quickly, colliding into a nearby tree. His hands reach backwards around the trunk."
    # Glitch OFF
    m "I - I..."
    m "Look, I don't know what I should do anymore."
    m "If I help Rohan, Sabie complains. If I help Sabie, Rohan complains. If I leave you both alone, you both complain."
    m "I can't win. So, stop trying to make me play your fucking game, okay?"

    jump lunch_1b

label lunch_1b:

    show rohan sad at right
    show sabie worried at left

    r "..."
    s "..."

    show tyree worried
    hide rohan
    hide sabie

    t "..."

    hide tyree
    show rohan sad at right
    show sabie worried at left

    n "Sabie lets go of the phone and nudges it back to Rohan. Rohan quietly pockets it, eyes trained on Masami."
    s "{i}Ge{/i}. What happened last night?"
    m "Last night?"
    s "Something happened last night or you wouldn't be acting like this."
    n "Masami inhales slowly."
    m "Nothing happened. I have no idea what you're talking about."

    show sabie annoyed at center with move
    show rohan neutral

    n "Sabie gets up and walks over to him very slowly, her fists balled."
    n "She stops when she's inches away and stares up at him, unflinching."
    s "Don't even try that on me, dumbass. I thought you knew better than that."
    n "She pokes him hard on the forehead."
    m "Ow! What was that for?"
    s "Your idiocy."
    s worried "Look, I really didn't want things to go this way, but you're not giving me a choice."
    s "I let you get away with holding those stupid thoughts in your head last time."

    # Glitch ON - will stay on until Masami enters house
    s mischievous  "And what did you do?"
    hide rohan with Dissolve(1.0) # TODO: Fix transition!

    # Depends if you visited Alyssa first or not
    if alyssa_visit_first:

        s innocent "You ditch the girl you've been pining over for years as if it were nothing."
        s happy "I'll give you credit for even having the balls to go straight to her in the first place."
        s "But still."

    else:

        s innocent "You waste so much time trying to decide whether or not you actually want to get the idiot you've been pining over for years."
        s happy "Then after you finally work up the fucking nerve, you just ditch her."

    s mischievous "Incredibly rude."
    s "Waste of my efforts."

    # Depends if you trusted Sabie with the Xinyi response earlier on Day 3 - Before
    if sabie_trust:

        s happy "You told me something was wrong before and I supported you."
        s "What about that wasn't enough for you that you had to clam up like that?"

    else:

        s happy "Don't you care that there are people out here trying to help you at all?"
        s "Was it worth it being so damn selfish that you couldn't even bother to explain yourself? Not even to me when I fucking asked you what was wrong?"

    s "What on earth is going on in your head that's worth keeping from the rest of us?"
    m "I - "
    m "I don’t know."

    jump lunch_1c

label lunch_1c:

    s mischievous "Pft. Of course you know yourself, silly."

    # Depends on if you answered Sabie's message on Day 2 - After
    if sabie_respond:
        s "The day after you painted that wall with your word vomit, you had the audacity to text me like everything was perfectly normal."
        s "How sick of you think you could hide such a monster from yourself."
    else:
        s "You knew enough that you decided to leave me on read. On read!"
        s "On no circumstance do you ever leave some on read, even if they fucked up and sent a deleted message to you."
        s "You have to at least leave an emoji."

    s happy "Sometimes, I really can't believe you."

    m "But - "

    # Depends on if you answered Rohan's message

    show rohan annoyed at right with Dissolve(1.0)

    r "Don't even try lying to yourself."
    r sad "Just look at how you've treated me!"

    if rohan_respond:
        r "You respond to my photos just to be nice. I know that you do."
        r "You wouldn't dare tell me otherwise or you think I'll go even further off the rails."
        r "Just like your sister. And you didn't want that happening, did you?"
    else:
        r "You couldn't even spend a moment to look at a single photo."
        r "It wasn't even much to ask for. Just a glance to say that you supported me when I needed it."

    r happy "But definitely, believe what you want. That you actually look good in the eyes of others."
    r "Keep your pathetic little image of yourself as the golden boy."

    m "What are you talking about?"
    m "Of course I'm not perfect! Of all people, you'd think I know that by now."

    # Depends on if you answered Tyree's message

    show tyree at left with Dissolve(1.0)

    t "We know you aren't."
    t worried "But that's the problem lies, I'm afraid."

    if tyree_respond:
        t "You always care too much about what others think."
        t "What's more is that you take on more than what you can give."
    else:
        t "You don't think enough of others to offer gratitude for when they do offer to help."
        t "When the world gives you its favor, you wallow in self-pity. And when you do not succeed, you bury yourself even deeper."
        t "Nothing is ever enough for you and in your cowardice, you will never be satisfied."

    # TODO: Change Tyree's expression to happy and add dialogue to adjust flow, address secrets kept, etc.

    m "Please, I - "
    n "Masami looks desperately around. His arms lock tighter around the trunk."
    n "Sabie laughs and shakes her head." # Integrate this!
    s "If you don't trust us, just say so. At least you're being honest."
    s "Not like whatever shit you're trying to pull with yourself."
    m "I - "
    n "In the distance, the school bell rings."
    m "I gotta go."
    n "Before any of them can stop him, Masami makes a break for entrance inside."

    jump hallway_1

# Masami runs into Nasir
label hallway_1:

    scene bg black with Dissolve(0.5)
    scene bg hallway with Dissolve(0.5)

    n "He pushes open the door and tries to lose himself in the crowd."
    n "Behind him, he can hear Sabie's footsteps hot on his heels."
    s "Oi, dumbass!"
    s "You can't run from yourself forever!"
    m "(I'm not running from myself. I'm not.)"
    m "(I'm just...)"
    m "..."
    m "(Damn it.)"
    n "Masami quickens his pace, weaving in between the molasses slow current of people."
    m "(Can't everyone just leave me alone?)"
    m "(Nothing happened, nothing changed.)"
    m "(So why can't I just - )"
    n "He turns a corner and brushes a little too hard against an unsuspecting student."
    m "Ah, sorry - "
    n "Masami freezes."
    m "Oh."

    show nasir surprised at right with Dissolve(0.1)
    # TODO: Add Alyssa in here too!

    a "Ugh, you again?"
    a "Got some nerve to show up, huh."
    m "Alyssa - "
    a "Oh, I know what you came for now."
    # Alyssa gives Nasir a little push
    a "Go on, take your boyfriend and be happy. That's what you want, right?"
    m "The hell? I never - "
    a "Spare me. I've had enough of you, cheating scum."
    m "No, Alyssa, please - "
    m "I didn't mean - "
    na sad "It's alright."

    show nasir surprised at center with move

    n "Nasir looks away and also moves to leave, but Masami moves to grab his wrist."
    m "Wait!"
    na sad "What is it?"
    m "About last night. I - "
    na happy "You don't need to explain. I understand."
    na sad "But perhaps you could have been more honest with yourself."

    if kiss:
        na "You should have pushed me away earlier if you didn't want me."
        na "You shouldn't have kissed me back as if it meant something."

    else:
        # If a cookie was taken
        if take_cookie:
            na "Perhaps I should have known better than to judge from a simple gesture of taking a cookie."
        else:
            na "I should have known when you refused to take a cookie."
            na "But then, you led me on the whole night with the journey and conversation. And I thought, maybe, we did feel the same way about each other."
            na "Do you know how betrayed I felt when you couldn't do something so simple at the end?"
            na "Is a kiss really too much go give?"

    m "I - I wasn't thinking straight. Neither of us were."
    m "I'm trying to tell you what I really want now. And that's - "

    if kiss:

        na "What?"
        m "…I think I like you. The same way. I just didn't realize until last night."
        na "Ah."
        m "That's it? Your only response? Isn't this suppose to be a mutual feeling where we're both supposed to be excited?"
        na "Perhaps."
        na "But let me ask you this: if we start something, would you be ready to tell your friends and family about it?"
        na "Even if they would reject you?"
        na "Is that something you could truly ask of yourself when you don’t even have the courage to speak up for your own sister?"
        m "…"
        na "That's what I was afraid of."

    else:
        na "You've already made yourself clear enough."

    na "Goodbye Masami."

    hide nasir with Dissolve(1.0)

    n "With that, Nasir twists his arm free and disappears into the outgoing stream of people."
    m "..."

    jump masami_kitchen_1

# Blackout scene change back to house
# Glitch OFF
label masami_kitchen_1:

    stop music fadeout 1.5
    scene bg black with Dissolve(1.5)
    scene bg kitchen with Dissolve(1.5)
    play music emotional fadein 1.0

    mm "Hello Masami! Welcome home!"
    m "…"
    mm "Something wrong?"
    m "Not really, no."
    n "Masami glances at the stovetop."
    m "Making the ginger duck hotpot so soon?"
    n "Masami's mother laughs."
    mm "Well you made a lot of {i}tangyuan{/i}. So I think, why not start making soup?"
    m "Oh."
    mm "We can always make more tomorrow {i}tangyuan{/i} to cook tomorrow, don't worry!"
    m "Of course."
    n "She pats him heartily on the back."
    mm "You excited to eat? Have family time?"
    m "Yeah. I think so."
    m "That would be nice. I couldn't wish for more than that."
    m "(I just such a wish was worth having to begin with.)"

    stop music fadeout 2.0
    scene bg black with Dissolve(2.0)

    jump tangyuan_cook
