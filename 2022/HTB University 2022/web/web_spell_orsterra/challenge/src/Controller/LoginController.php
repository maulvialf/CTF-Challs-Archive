<?php

namespace App\Controller;

use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\HttpFoundation\Request;
use Doctrine\Persistence\ManagerRegistry;
use App\Entity\User;

class LoginController extends AbstractController
{
    public function login(Request $request, ManagerRegistry $doctrine)
    {
        if ($request->get('username') && $request->get('password'))
        {
            $user = $doctrine->getRepository(User::class)->loginUser
            (
                $request->get('username'),
                $request->get('password')
            );
            if ( $user )
            {
                $request->getSession()->set('loggedin', true);
                return $this->redirect('/admin/');
            }
            return $this->redirect('/?msg=login failed');
        }
        return $this->redirect('/?msg=Please login first!');
    }

}
