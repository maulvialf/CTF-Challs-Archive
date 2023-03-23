using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Run : MonoBehaviour
{

    public Vector3 startingPos;
    public GameObject spaceshipFab;
    public TrackScript track;
    public GameObject spaceship;
    AISpaceShipController spaceshipController;
    public TargetCamera bestCamera;
    SpaceShipCheckPoint checkpoint;
    void Start()
    {
        
        spaceshipController = new AISpaceShipController();

        checkpoint = spaceshipFab.GetComponent<SpaceShipCheckPoint>();
        checkpoint.track = track;

        spaceship = Instantiate(spaceshipFab, startingPos, spaceshipFab.transform.rotation);
        spaceshipController = spaceship.GetComponent<AISpaceShipController>();
        bestCamera.target = spaceshipController.transform;
        spaceshipController.Stop();
        Application.targetFrameRate = 10;
        Debug.Log("Setup ready.");
    }

    void LoadNeural(string message)
    {
        AISpaceShipController carController = spaceship.GetComponent<AISpaceShipController>();
        carController.network = new NeuralNetwork(message);
        carController.Reset(spaceship.transform.position, spaceship.transform.rotation);
        spaceship.GetComponent<SpaceShipCheckPoint>().currentLap = 0;
    }

    void Update()
    {
        int lap = spaceship.GetComponent<SpaceShipCheckPoint>().currentLap;
        if (lap == 1)
        {      
            Debug.Log("Flag will appear here");
            spaceshipController.Stop();
            Time.timeScale = 0;
            spaceship.GetComponent<SpaceShipCheckPoint>().currentLap = 1337;
        }

    }
}
