const sendme = () => {
    var name = document.getElementById('name').value
    var pass = document.getElementById('password').value

    console.log(name+'  '+pass)

    fetch(`${window.origin}/sendme`, {
        method: 'POST',
        credentials: 'include',
        body: JSON.stringify({ name: name, pass: pass }),
        cache: 'no-cache',
        headers: new Headers(
            { 'content-type': 'application/json' }
        )
    }

    ).then((res) => {
        console.log(res)
    })
}