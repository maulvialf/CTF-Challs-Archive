<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\User;
use Auth;

class HomeController extends Controller
{
    /**
     * Create a new controller instance.
     *
     * @return void
     */
    public function __construct()
    {
        $this->middleware('auth');
    }

    /**
     * Show the application dashboard.
     *
     * @return \Illuminate\Contracts\Support\Renderable
     */
    public function index()
    {
        $refCount = User::where('referer', Auth::user()->email)->count();
        if ($refCount >= 15) {
            $flag = 'redmask{beaware_for_allowing_email_alias}';
        } else {
            $flag = "anda belum memiliki cukup pengikut!";
        }
        return view('home')->with([
            'referer' => $refCount,
            'flag' => $flag
        ]);
    }
}
