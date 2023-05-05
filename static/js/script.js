function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');



function addToCart(e){
    let feature_id = e
    let url = "add_to_cart/"

    let data = {id:feature_id}

    fetch(url, {
        method: "POST",
        headers: {"Content-Type":"application/json", 'X-CSRFToken' : csrftoken},
        body: JSON.stringify(data)
    })
    .then(res=>res.json())
    .then(data=>{
        console.log(data)
    })
    .catch(error=>{
        console.log(error)
    })
}


function removeFromCart(e){
    let item_id = e
    let url = "remove_from_cart/"

    let data = {id:item_id}

    fetch(url, {
        method: "POST",
        headers: {"Content-Type":"application/json", 'X-CSRFToken' : csrftoken},
        body: JSON.stringify(data)
    })
    .then(res=>res.json())
    .then(data=>{
        console.log(data)
        location.reload()
    })
    .catch(error=>{
        console.log(error)
    })
}