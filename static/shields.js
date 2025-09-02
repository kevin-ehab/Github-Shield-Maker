const badgeButtons = document.querySelectorAll('.badge-btn')
const syntaxBox = document.getElementById('syntax')
const copyBtn = document.getElementById('copy')
copyBtn.disabled = true

badgeButtons.forEach(button => {
    button.addEventListener('click', ()=>{  
        let badge = button.dataset.badge
        syntaxBox.style.color = 'black'
        syntaxBox.innerText = badge
        copyBtn.disabled = false
    })
})

copyBtn.addEventListener('click', ()=>{
    let text = syntaxBox.innerText
    navigator.clipboard.writeText(text)
    syntaxBox.innerText = "Copied Successfully!"
    syntaxBox.style.color = 'green'
})
