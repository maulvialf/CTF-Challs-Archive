using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class SpaceShipCheckPoint : MonoBehaviour
{
    public SpaceShipController spaceshipController;
    public TrackScript track;
    public Transform[] checkpointArray;
    public int nextCheckpoint = 17;
    public int currentLap = -1;
    public float distanceToCheckpoint;

    public Text checkPointText;

    
    void Start(){
        checkpointArray = track.checkpointArray;
        distanceToCheckpoint = Vector2.Distance(spaceshipController.spaceship.position, checkpointArray[nextCheckpoint].position);
    }

    
    void Update(){
        distanceToCheckpoint = Vector2.Distance(spaceshipController.spaceship.position, checkpointArray[nextCheckpoint].position);
    }
}
