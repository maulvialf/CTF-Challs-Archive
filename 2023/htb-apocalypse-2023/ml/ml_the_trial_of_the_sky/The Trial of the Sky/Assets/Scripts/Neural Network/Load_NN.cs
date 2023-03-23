using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System.Runtime.InteropServices;
using JetBrains.Annotations;

public class Load_NN : MonoBehaviour
{
    
    [DllImport("__Internal")]
    public static extern string BrowserTextUpload(string extFilter, string gameObjName, string dataSinkFn);
    // Start is called before the first frame update
    void Start()
    {

    }

    // Update is called once per frame
    void Update()
    {

    }
    //The following will only work on WebGL builds
    public void OnButton_UploadDocument()
    {
        BrowserTextUpload(".txt", "Run", "LoadNeural");
        Time.timeScale = 2.0f;
    }
}

