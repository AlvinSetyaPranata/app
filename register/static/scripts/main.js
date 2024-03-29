const form = document.getElementsByTagName("form")[0]

form.addEventListener("submit", (e) => {
    e.preventDefault()

    const data = {
        "siswa" : {},
        "ayah" : {},
        "ibu" : {}
    }


    const formData = new FormData()

    Object.values(e.target).map(input => {
        const fieldName = input.name

        if (fieldName.startsWith("student")) {
            data["siswa"][fieldName.split("-", 1)[1]] = input.value
        }
        else if (fieldName.startsWith("father")) {
            data["ayah"][fieldName.split("-")[1]] = input.value
        }
        else if (fieldName.startsWith("mother")) {
            data["ibu"][fieldName.split("-", 1)[1]] = input.value
        }
    })


    formData.append("csrfmiddlewaretoken", form[0].value)
    formData.append("siswa", JSON.stringify(data["siswa"]))
    formData.append("ayah", JSON.stringify(data["ayah"]))
    formData.append("ibu", JSON.stringify(data["ibu"]))

    fetch("", {
        method: "POST",
        body: formData
    }).then((res) => console.log(res))

})
