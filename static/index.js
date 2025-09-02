const urlInput = document.getElementById('url')
const colorSelect = document.getElementById('colorSelect')
const generateButton = document.getElementById('generate')

generateButton.addEventListener('click', () =>{
    link = urlInput.value
    color = colorSelect.value

    fetch('/shields', {
        method: 'POST',
        headers: {"Content-Type":"application/json"},
        body: JSON.stringify({link, color})
    })
    .then(res => res.json())
    .then(data => {
        console.log(data.message)
        window.location = '/generated'
    })
})