export default function Navbar(){
    return(
        <>
            <div className="flex justify-between p-2">
                <div className="logo flex">
                    {/* <img className="w-10 h-10 object-cover object-center" src="./menu-bar.png"></img> */}
                    <img className="w-12 h-12 rounded-full object-cover object-center" src="./pf.jpeg"></img>
                </div>
                <div className="icons flex gap-2.5">
                    <img className="w-10 h-10 object-cover object-center" src="./bell.png"></img>
                    <img className="w-10 h-10 object-cover object-center" src="./settings.png"></img>
                    <img className="w-10 h-10 object-cover object-center" src="./weather.png"></img>
                    <img className="w-10 h-10 object-cover object-center" src="./user.png"></img>
                </div>
                
            </div>
        </>
    )
}