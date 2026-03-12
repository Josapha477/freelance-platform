


const menu_toggle = document.getElementById("menu-toggle");

const path = document.getElementById("mypath")

const menu = document.getElementById("mobile-menu");

const togglemode = document.getElementById("toggleMode")

menu_toggle.addEventListener( 'click', function ()
{
    if ( menu.classList.contains( "hidden" ) )
    {
        menu.classList.toggle( "hidden" );
        path.setAttribute("d", "M6 18L18 6M6 6l12 12")
    } else
    {
        menu.classList.toggle( "hidden" );
        path.setAttribute("d", "M4 6h16M4 12h16M4 18h16")
    }

} );


togglemode.addEventListener( "click", () =>
{
    document.body.classList.toggle( "dark-mode" );
    console.log(document.body)
})







