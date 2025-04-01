#function growthMindsetChallenge() {
    const challenges = {
        1: "Learn something new (watch a short tutorial or read an article).",
        2: "Embrace a mistake—write down what you learned from it.",
        3: "Replace 'I can\\'t' with 'I can\\'t yet' in one situation.",
        4: "Ask for feedback and thank the person, even if it's tough.",
        5: "Try a different approach to a problem you're stuck on.",
        6: "Celebrate someone else’s success—no jealousy!",
        7: "Reflect: How did your mindset shift this week?"
    };
    
    console.log("🌟 7-Day Growth Mindset Challenge 🌟");
    for (let day in challenges) {
        prompt(`Day ${day}: ${challenges[day]}\nPress OK when done.`);
    }
    console.log("🎉 Challenge complete! Keep growing! 💪");
}

growthMindsetChallenge();
