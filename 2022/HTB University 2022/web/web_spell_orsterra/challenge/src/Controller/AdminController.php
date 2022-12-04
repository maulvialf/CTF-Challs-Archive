<?php

namespace App\Controller;

use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\Session\SessionInterface;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\RequestStack;
use Symfony\Component\Messenger\MessageBusInterface;
use Doctrine\Persistence\ManagerRegistry;
use Symfony\Component\Validator\Constraints as Assert;
use Symfony\Component\Validator\Validator\ValidatorInterface;
use App\Message\SubscribeNotification;
use App\Repository\TrackerRepository;
use App\Repository\SpellServiceRepository;
use App\Entity\Tracker;
use App\Entity\SpellService;

class AdminController extends AbstractController
{
    private $isLoggedIn;
    private $validator;

    public function __construct(RequestStack $requestStack, ValidatorInterface $validator)
    {
        $this->session = $requestStack->getSession();
        $this->isLoggedIn = $this->session->get('loggedin');
        $this->validator = $validator;
    }

    public function adminIndex(Request $request)
    {
        if (!$this->isLoggedIn)
        {
            return $this->redirect('/login?msg=please login first');
        }

        return $this->render('site/admin.html');
    }

    public function exportIndex(Request $request,  SpellServiceRepository $repository)
    {
        if (!$this->isLoggedIn)
        {
            return $this->redirect('/login?msg=please login first');
        }

        return $this->render('site/exports.html');
    }

    public function listExports(Request $request, SpellServiceRepository $repository)
    {
        if (!$this->isLoggedIn)
        {
            return $this->redirect('/login?msg=please login first');
        }

        $Subscribers = $repository->findAll();
        $exportList = array();

        foreach($Subscribers as $item)
        {
            $exportMap = md5($item->getTrackUUID()) . '.png';
            $exportFile = '/www/public/static/exports/' . $exportMap;

            if ( ! file_exists($exportFile) ) $exportMap = null;

            $exportList[] = array(
                'uuid'       => $item->getTrackUUID(),
                'email'      => $item->getEmail(),
                'export_map' => $exportMap
            );
        }

        return $this->json($exportList);
    }


    public function listTracker(Request $request, TrackerRepository $repository)
    {
        if (!$this->isLoggedIn)
        {
            return $this->redirect('/login?msg=please login first');
        }

        $Trackers = $repository->findAll();
        $TrackersList = array();

        foreach($Trackers as $item)
        {
            $TrackersList[] = array(
                'uuid'         => $item->getUUID(),
                'y-coordinate' => (int)$item->getYCoordinate(),
                'x-coordinate' => (int)$item->getXCoordinate(),
                'live-spell'   => (int)$item->getLiveSpell(),
            );
        }

        return $this->json($TrackersList);
    }

    public function subscribe(Request $request, ManagerRegistry $doctrine, MessageBusInterface $bus)
    {
        if (!$this->isLoggedIn)
        {
            return $this->redirect('/login?msg=please login first');
        }

        $subscribe = json_decode($request->getContent(), false);

        if (!(
            property_exists($subscribe, "email") &&
            property_exists($subscribe, "uuid")
        ))
        {
            return $this->json(["message" => "Missing required parameters!"], 500);
        }

        // validate email
        $emailConstraint = new Assert\Email();

        $errors = $this->validator->validate(
            $subscribe->email,
            $emailConstraint
        );

        if ($errors->count())
        {
            return $this->json(["message" => "Invalid email address supplied!"], 401);
        }

        // validate tracker uuid
        $entityManager = $doctrine->getManager();
        $tracker = $entityManager->getRepository(Tracker::class)->findOneByUUID($subscribe->uuid);

        if (!$tracker) {
            return $this->json(["message" => "This tracker uuid doesn't exist!"], 500);
        }

        // change live spell status
        $tracker->setLiveSpell(1);

        // insert spell service
        $entityManager = $doctrine->getManager();

        $spellServiceEntity = new SpellService();
        $spellServiceEntity->setEmail($subscribe->email);
        $spellServiceEntity->setTrackUUID($subscribe->uuid);

        $entityManager->persist($spellServiceEntity);
        $entityManager->flush();

        // dispatch notification
        $subscribeNotification = new SubscribeNotification(
            $subscribe->email,
            $subscribe->uuid,
            $tracker->getXCoordinate(),
            $tracker->getYCoordinate()
        );
        $bus->dispatch($subscribeNotification);

        return $this->json(["message" => "Email subscribed successfully!"]);

    }

    public function logout(Request $request)
    {
        $request->getSession()->invalidate();;
        return $this->redirect('/');
    }


}