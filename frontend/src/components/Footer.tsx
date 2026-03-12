

export default function Footer() {

    return (
        <footer className="bg-gray-900 text-gray-400 py-16">
            <div className="max-w-7xl mx-auto px-6 grid
                md:grid-cols-4 gap-10
            ">
                <div>
                    <h1 className="text-white 
                    mb-4 text-xl font-bold">Aster</h1>
                    <p>Votre partenaire qui vous accompagnes</p>
                </div>
                <div>
                    <h4 className="text-white mb-4 
                    font-semibold">Produit</h4>
                    <ul className="space-y-2">
                        <li><a href="#">Fonctionnalites</a></li>
                        <li><a href="#">Tarifs</a></li>
                    </ul>
                </div>
                 <div>
                    <h4 className="text-white mb-4 
                    font-semibold">Entreprise</h4>
                    <ul className="space-y-2">
                        <li><a href="#">A propos</a></li>
                        <li><a href="#">Blog</a></li>
                    </ul>
                </div>
                <div>
                    <h4 className="text-white mb-4 font-semibold
                    ">Contact</h4>
                    <p>Email: contact@asternova@gmail.com</p>
                </div>

            </div>
        </footer>
    )
}