import { Link } from "react-router-dom";

type Props = {
    freelance: {
        id: number;
        avatar: string;
        last_name: string;
        first_name: string;
        bio: string;
        available_hour_per_week: number;
        hourly_rate: number;
        year_experience: number;
        country: string;
    }
}

export const ProfileCard = ({freelance}: Props) => {
    return (
        <div className="flex text-blue-500 text-center
         md:text-green-500 sm:text-yellow-500
         xl:text-red-500 justify-center">
            <div className="rounded-2xl shadow-md
            hover:shadow-lg transition-shadow p-6 bg-white w-full">
                <div className="flex items-center gap-4">
                    <div className="w-12 h-12 rounded-full bg-blue-600
                    text-white flex items-center justify-center font-bold
                    text-lg">
                        JM
                    </div>
                    <div>
                        <h3 className="text-lg font-semibold text-gray-800">
                            {freelance.first_name} {freelance.last_name}
                        </h3>
                        <p className="text-sm text-blue-600 font-meduim">
                            Developpeur Full-Stack
                        </p>
                    </div>
                </div>
                <p className="mt-4 text-sm text-gray-600 leading-relaxed">
                    {freelance.bio}
                </p>
                <div className="mt-4 flex flex-wrap gap-2">
                    <span className="px-3 py-1 text-xs rounded-full bg-blue-100
                    text-blue-700">
                        React
                    </span>
                    <span className="px-3 py-1 text-xs rounded-full bg-blue-100
                    text-blue-700">
                        Django
                    </span>
                    <span className="px-3 py-1 text-xs rounded-full bg-blue-100
                    text-blue-700">
                        GraphQL
                    </span>
                </div>
                <div className="mt-6">
                    <Link to={`/profile/${freelance.id}`} className="w-full bg-blue-600 text-white py-2 rounded-xl
                    font-medium hover:bg-blue-700 transition-colors">
                        Voir le profil
                    </Link>
                </div>
            </div>

        </div>


//         <a href="#" className="hover-3d my-12 mx-2 cursor-pointer">
  
//   {/* content */}
//   <div className="card w-96 bg-black text-white bg-[radial-gradient(circle_at_bottom_left,#ffffff04_35%,transparent_36%),radial-gradient(circle_at_top_right,#ffffff04_35%,transparent_36%)] bg-size-[4.95em_4.95em]">
//     <div className="card-body">
//       <div className="flex justify-between mb-10">
//         <div className="font-bold">BANK OF LATVERIA</div>
//         <div className="text-5xl opacity-10">❁</div>
//       </div>
//       <div className="text-lg mb-4 opacity-40">0210 8820 1150 0222</div>
//       <div className="flex justify-between">
//         <div>
//           <div className="text-xs opacity-20">CARD HOLDER</div>
//           <div>VICTOR VON D.</div>
//         </div>
//         <div>
//           <div className="text-xs opacity-20">EXPIRES</div>
//           <div>29/08</div>
//         </div>
//       </div>
//     </div>
//   </div>
  
//   {/* 8 empty divs needed for the 3D effect */}
//   <div></div>
//   <div></div>
//   <div></div>
//   <div></div>
//   <div></div>
//   <div></div>
//   <div></div>
//   <div></div>
// </a>
       
    )
}