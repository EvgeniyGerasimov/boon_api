LESSON_STRUCTURE = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "data": {
      "type": "object",
      "properties": {
        "viewer": {
          "type": "object",
          "properties": {
            "sections": {
              "type": "array",
              "items": [
                {
                  "type": "object",
                  "properties": {
                    "id": {
                      
                    },
                    "name": {
                      
                    },
                    "lessons": {
                      "type": "array",
                      "items": [
                        {
                          "type": "object",
                          "properties": {
                            "id": {
                              
                            },
                            "name": {
                              
                            },
                            "finalAssessment": {
                              
                            },
                            "subLessons": {
                              "type": "array",
                              "items": [
                                {
                                  "type": "object",
                                  "properties": {
                                    "id": {
                                      
                                    },
                                    "name": {
                                      
                                    },
                                    "isCompleted": {
                                      "type": "boolean"
                                    },
                                    "quizzes": {
                                      "type": "array",
                                      "items": [
                                        {
                                          "type": "object",
                                          "properties": {
                                            "id": {
                                              
                                            },
                                            "viewerRelated": {
                                              "type": "object",
                                              "properties": {
                                                "isCompleted": {
                                                  "type": "boolean"
                                                }
                                              },
                                              "required": [
                                                "isCompleted"
                                              ]
                                            }
                                          },
                                          "required": [
                                            "id",
                                            "viewerRelated"
                                          ]
                                        }
                                      ]
                                    }
                                  },
                                  "required": [
                                    "id",
                                    "name",
                                    "isCompleted",
                                    "quizzes"
                                  ]
                                },
                                {
                                  "type": "object",
                                  "properties": {
                                    "id": {
                                      
                                    },
                                    "name": {
                                      
                                    },
                                    "isCompleted": {
                                      "type": "boolean"
                                    },
                                    "quizzes": {
                                      "type": "array",
                                      "items": [
                                        {
                                          "type": "object",
                                          "properties": {
                                            "id": {
                                              
                                            },
                                            "viewerRelated": {
                                              "type": "object",
                                              "properties": {
                                                "isCompleted": {
                                                  "type": "boolean"
                                                }
                                              },
                                              "required": [
                                                "isCompleted"
                                              ]
                                            }
                                          },
                                          "required": [
                                            "id",
                                            "viewerRelated"
                                          ]
                                        }
                                      ]
                                    }
                                  },
                                  "required": [
                                    "id",
                                    "name",
                                    "isCompleted",
                                    "quizzes"
                                  ]
                                },
                                {
                                  "type": "object",
                                  "properties": {
                                    "id": {
                                      
                                    },
                                    "name": {
                                      
                                    },
                                    "isCompleted": {
                                      "type": "boolean"
                                    },
                                    "quizzes": {
                                      "type": "array",
                                      "items": [
                                        {
                                          "type": "object",
                                          "properties": {
                                            "id": {
                                              
                                            },
                                            "viewerRelated": {
                                              "type": "object",
                                              "properties": {
                                                "isCompleted": {
                                                  "type": "boolean"
                                                }
                                              },
                                              "required": [
                                                "isCompleted"
                                              ]
                                            }
                                          },
                                          "required": [
                                            "id",
                                            "viewerRelated"
                                          ]
                                        }
                                      ]
                                    }
                                  },
                                  "required": [
                                    "id",
                                    "name",
                                    "isCompleted",
                                    "quizzes"
                                  ]
                                }
                              ]
                            }
                          },
                          "required": [
                            "id",
                            "name",
                            "finalAssessment",
                            "subLessons"
                          ]
                        },
                        {
                          "type": "object",
                          "properties": {
                            "id": {
                              
                            },
                            "name": {
                              
                            },
                            "finalAssessment": {
                              
                            },
                            "subLessons": {
                              "type": "array",
                              "items": [
                                {
                                  "type": "object",
                                  "properties": {
                                    "id": {
                                      
                                    },
                                    "name": {
                                      
                                    },
                                    "isCompleted": {
                                      "type": "boolean"
                                    },
                                    "quizzes": {
                                      "type": "array",
                                      "items": [
                                        {
                                          "type": "object",
                                          "properties": {
                                            "id": {
                                              
                                            },
                                            "viewerRelated": {
                                              "type": "object",
                                              "properties": {
                                                "isCompleted": {
                                                  "type": "boolean"
                                                }
                                              },
                                              "required": [
                                                "isCompleted"
                                              ]
                                            }
                                          },
                                          "required": [
                                            "id",
                                            "viewerRelated"
                                          ]
                                        }
                                      ]
                                    }
                                  },
                                  "required": [
                                    "id",
                                    "name",
                                    "isCompleted",
                                    "quizzes"
                                  ]
                                },
                                {
                                  "type": "object",
                                  "properties": {
                                    "id": {
                                      
                                    },
                                    "name": {
                                      
                                    },
                                    "isCompleted": {
                                      "type": "boolean"
                                    },
                                    "quizzes": {
                                      "type": "array",
                                      "items": [
                                        {
                                          "type": "object",
                                          "properties": {
                                            "id": {
                                              
                                            },
                                            "viewerRelated": {
                                              "type": "object",
                                              "properties": {
                                                "isCompleted": {
                                                  "type": "boolean"
                                                }
                                              },
                                              "required": [
                                                "isCompleted"
                                              ]
                                            }
                                          },
                                          "required": [
                                            "id",
                                            "viewerRelated"
                                          ]
                                        }
                                      ]
                                    }
                                  },
                                  "required": [
                                    "id",
                                    "name",
                                    "isCompleted",
                                    "quizzes"
                                  ]
                                },
                                {
                                  "type": "object",
                                  "properties": {
                                    "id": {
                                      
                                    },
                                    "name": {
                                      
                                    },
                                    "isCompleted": {
                                      "type": "boolean"
                                    },
                                    "quizzes": {
                                      "type": "array",
                                      "items": [
                                        {
                                          "type": "object",
                                          "properties": {
                                            "id": {
                                              
                                            },
                                            "viewerRelated": {
                                              "type": "object",
                                              "properties": {
                                                "isCompleted": {
                                                  "type": "boolean"
                                                }
                                              },
                                              "required": [
                                                "isCompleted"
                                              ]
                                            }
                                          },
                                          "required": [
                                            "id",
                                            "viewerRelated"
                                          ]
                                        }
                                      ]
                                    }
                                  },
                                  "required": [
                                    "id",
                                    "name",
                                    "isCompleted",
                                    "quizzes"
                                  ]
                                }
                              ]
                            }
                          },
                          "required": [
                            "id",
                            "name",
                            "finalAssessment",
                            "subLessons"
                          ]
                        },
                        {
                          "type": "object",
                          "properties": {
                            "id": {
                              
                            },
                            "name": {
                              
                            },
                            "finalAssessment": {
                              
                            },
                            "subLessons": {
                              "type": "array",
                              "items": [
                                {
                                  "type": "object",
                                  "properties": {
                                    "id": {
                                      
                                    },
                                    "name": {
                                      
                                    },
                                    "isCompleted": {
                                      "type": "boolean"
                                    },
                                    "quizzes": {
                                      "type": "array",
                                      "items": [
                                        {
                                          "type": "object",
                                          "properties": {
                                            "id": {
                                              
                                            },
                                            "viewerRelated": {
                                              "type": "object",
                                              "properties": {
                                                "isCompleted": {
                                                  "type": "boolean"
                                                }
                                              },
                                              "required": [
                                                "isCompleted"
                                              ]
                                            }
                                          },
                                          "required": [
                                            "id",
                                            "viewerRelated"
                                          ]
                                        }
                                      ]
                                    }
                                  },
                                  "required": [
                                    "id",
                                    "name",
                                    "isCompleted",
                                    "quizzes"
                                  ]
                                },
                                {
                                  "type": "object",
                                  "properties": {
                                    "id": {
                                      
                                    },
                                    "name": {
                                      
                                    },
                                    "isCompleted": {
                                      "type": "boolean"
                                    },
                                    "quizzes": {
                                      "type": "array",
                                      "items": [
                                        {
                                          "type": "object",
                                          "properties": {
                                            "id": {
                                              
                                            },
                                            "viewerRelated": {
                                              "type": "object",
                                              "properties": {
                                                "isCompleted": {
                                                  "type": "boolean"
                                                }
                                              },
                                              "required": [
                                                "isCompleted"
                                              ]
                                            }
                                          },
                                          "required": [
                                            "id",
                                            "viewerRelated"
                                          ]
                                        }
                                      ]
                                    }
                                  },
                                  "required": [
                                    "id",
                                    "name",
                                    "isCompleted",
                                    "quizzes"
                                  ]
                                },
                                {
                                  "type": "object",
                                  "properties": {
                                    "id": {
                                      
                                    },
                                    "name": {
                                      
                                    },
                                    "isCompleted": {
                                      "type": "boolean"
                                    },
                                    "quizzes": {
                                      "type": "array",
                                      "items": [
                                        {
                                          "type": "object",
                                          "properties": {
                                            "id": {
                                              
                                            },
                                            "viewerRelated": {
                                              "type": "object",
                                              "properties": {
                                                "isCompleted": {
                                                  "type": "boolean"
                                                }
                                              },
                                              "required": [
                                                "isCompleted"
                                              ]
                                            }
                                          },
                                          "required": [
                                            "id",
                                            "viewerRelated"
                                          ]
                                        }
                                      ]
                                    }
                                  },
                                  "required": [
                                    "id",
                                    "name",
                                    "isCompleted",
                                    "quizzes"
                                  ]
                                }
                              ]
                            }
                          },
                          "required": [
                            "id",
                            "name",
                            "finalAssessment",
                            "subLessons"
                          ]
                        }
                      ]
                    }
                  },
                  "required": [
                    "id",
                    "name",
                    "lessons"
                  ]
                },
                {
                  "type": "object",
                  "properties": {
                    "id": {
                      
                    },
                    "name": {
                      
                    },
                    "lessons": {
                      "type": "array",
                      "items": [
                        {
                          "type": "object",
                          "properties": {
                            "id": {
                              
                            },
                            "name": {
                              
                            },
                            "finalAssessment": {
                              
                            },
                            "subLessons": {
                              "type": "array",
                              "items": [
                                {
                                  "type": "object",
                                  "properties": {
                                    "id": {
                                      
                                    },
                                    "name": {
                                      
                                    },
                                    "isCompleted": {
                                      "type": "boolean"
                                    },
                                    "quizzes": {
                                      "type": "array",
                                      "items": [
                                        {
                                          "type": "object",
                                          "properties": {
                                            "id": {
                                              
                                            },
                                            "viewerRelated": {
                                              "type": "object",
                                              "properties": {
                                                "isCompleted": {
                                                  "type": "boolean"
                                                }
                                              },
                                              "required": [
                                                "isCompleted"
                                              ]
                                            }
                                          },
                                          "required": [
                                            "id",
                                            "viewerRelated"
                                          ]
                                        }
                                      ]
                                    }
                                  },
                                  "required": [
                                    "id",
                                    "name",
                                    "isCompleted",
                                    "quizzes"
                                  ]
                                },
                                {
                                  "type": "object",
                                  "properties": {
                                    "id": {
                                      
                                    },
                                    "name": {
                                      
                                    },
                                    "isCompleted": {
                                      "type": "boolean"
                                    },
                                    "quizzes": {
                                      "type": "array",
                                      "items": [
                                        {
                                          "type": "object",
                                          "properties": {
                                            "id": {
                                              
                                            },
                                            "viewerRelated": {
                                              "type": "object",
                                              "properties": {
                                                "isCompleted": {
                                                  "type": "boolean"
                                                }
                                              },
                                              "required": [
                                                "isCompleted"
                                              ]
                                            }
                                          },
                                          "required": [
                                            "id",
                                            "viewerRelated"
                                          ]
                                        }
                                      ]
                                    }
                                  },
                                  "required": [
                                    "id",
                                    "name",
                                    "isCompleted",
                                    "quizzes"
                                  ]
                                },
                                {
                                  "type": "object",
                                  "properties": {
                                    "id": {
                                      
                                    },
                                    "name": {
                                      
                                    },
                                    "isCompleted": {
                                      "type": "boolean"
                                    },
                                    "quizzes": {
                                      "type": "array",
                                      "items": [
                                        {
                                          "type": "object",
                                          "properties": {
                                            "id": {
                                              
                                            },
                                            "viewerRelated": {
                                              "type": "object",
                                              "properties": {
                                                "isCompleted": {
                                                  "type": "boolean"
                                                }
                                              },
                                              "required": [
                                                "isCompleted"
                                              ]
                                            }
                                          },
                                          "required": [
                                            "id",
                                            "viewerRelated"
                                          ]
                                        }
                                      ]
                                    }
                                  },
                                  "required": [
                                    "id",
                                    "name",
                                    "isCompleted",
                                    "quizzes"
                                  ]
                                }
                              ]
                            }
                          },
                          "required": [
                            "id",
                            "name",
                            "finalAssessment",
                            "subLessons"
                          ]
                        },
                        {
                          "type": "object",
                          "properties": {
                            "id": {
                              
                            },
                            "name": {
                              
                            },
                            "finalAssessment": {
                              
                            },
                            "subLessons": {
                              "type": "array",
                              "items": [
                                {
                                  "type": "object",
                                  "properties": {
                                    "id": {
                                      
                                    },
                                    "name": {
                                      
                                    },
                                    "isCompleted": {
                                      "type": "boolean"
                                    },
                                    "quizzes": {
                                      "type": "array",
                                      "items": [
                                        {
                                          "type": "object",
                                          "properties": {
                                            "id": {
                                              
                                            },
                                            "viewerRelated": {
                                              "type": "object",
                                              "properties": {
                                                "isCompleted": {
                                                  "type": "boolean"
                                                }
                                              },
                                              "required": [
                                                "isCompleted"
                                              ]
                                            }
                                          },
                                          "required": [
                                            "id",
                                            "viewerRelated"
                                          ]
                                        }
                                      ]
                                    }
                                  },
                                  "required": [
                                    "id",
                                    "name",
                                    "isCompleted",
                                    "quizzes"
                                  ]
                                },
                                {
                                  "type": "object",
                                  "properties": {
                                    "id": {
                                      
                                    },
                                    "name": {
                                      
                                    },
                                    "isCompleted": {
                                      "type": "boolean"
                                    },
                                    "quizzes": {
                                      "type": "array",
                                      "items": [
                                        {
                                          "type": "object",
                                          "properties": {
                                            "id": {
                                              
                                            },
                                            "viewerRelated": {
                                              "type": "object",
                                              "properties": {
                                                "isCompleted": {
                                                  "type": "boolean"
                                                }
                                              },
                                              "required": [
                                                "isCompleted"
                                              ]
                                            }
                                          },
                                          "required": [
                                            "id",
                                            "viewerRelated"
                                          ]
                                        }
                                      ]
                                    }
                                  },
                                  "required": [
                                    "id",
                                    "name",
                                    "isCompleted",
                                    "quizzes"
                                  ]
                                }
                              ]
                            }
                          },
                          "required": [
                            "id",
                            "name",
                            "finalAssessment",
                            "subLessons"
                          ]
                        },
                        {
                          "type": "object",
                          "properties": {
                            "id": {
                              
                            },
                            "name": {
                              
                            },
                            "finalAssessment": {
                              
                            },
                            "subLessons": {
                              "type": "array",
                              "items": [
                                {
                                  "type": "object",
                                  "properties": {
                                    "id": {
                                      
                                    },
                                    "name": {
                                      
                                    },
                                    "isCompleted": {
                                      "type": "boolean"
                                    },
                                    "quizzes": {
                                      "type": "array",
                                      "items": [
                                        {
                                          "type": "object",
                                          "properties": {
                                            "id": {
                                              
                                            },
                                            "viewerRelated": {
                                              "type": "object",
                                              "properties": {
                                                "isCompleted": {
                                                  "type": "boolean"
                                                }
                                              },
                                              "required": [
                                                "isCompleted"
                                              ]
                                            }
                                          },
                                          "required": [
                                            "id",
                                            "viewerRelated"
                                          ]
                                        }
                                      ]
                                    }
                                  },
                                  "required": [
                                    "id",
                                    "name",
                                    "isCompleted",
                                    "quizzes"
                                  ]
                                },
                                {
                                  "type": "object",
                                  "properties": {
                                    "id": {
                                      
                                    },
                                    "name": {
                                      
                                    },
                                    "isCompleted": {
                                      "type": "boolean"
                                    },
                                    "quizzes": {
                                      "type": "array",
                                      "items": [
                                        {
                                          "type": "object",
                                          "properties": {
                                            "id": {
                                              
                                            },
                                            "viewerRelated": {
                                              "type": "object",
                                              "properties": {
                                                "isCompleted": {
                                                  "type": "boolean"
                                                }
                                              },
                                              "required": [
                                                "isCompleted"
                                              ]
                                            }
                                          },
                                          "required": [
                                            "id",
                                            "viewerRelated"
                                          ]
                                        }
                                      ]
                                    }
                                  },
                                  "required": [
                                    "id",
                                    "name",
                                    "isCompleted",
                                    "quizzes"
                                  ]
                                },
                                {
                                  "type": "object",
                                  "properties": {
                                    "id": {
                                      
                                    },
                                    "name": {
                                      
                                    },
                                    "isCompleted": {
                                      "type": "boolean"
                                    },
                                    "quizzes": {
                                      "type": "array",
                                      "items": [
                                        {
                                          "type": "object",
                                          "properties": {
                                            "id": {
                                              
                                            },
                                            "viewerRelated": {
                                              "type": "object",
                                              "properties": {
                                                "isCompleted": {
                                                  "type": "boolean"
                                                }
                                              },
                                              "required": [
                                                "isCompleted"
                                              ]
                                            }
                                          },
                                          "required": [
                                            "id",
                                            "viewerRelated"
                                          ]
                                        }
                                      ]
                                    }
                                  },
                                  "required": [
                                    "id",
                                    "name",
                                    "isCompleted",
                                    "quizzes"
                                  ]
                                },
                                {
                                  "type": "object",
                                  "properties": {
                                    "id": {
                                      
                                    },
                                    "name": {
                                      
                                    },
                                    "isCompleted": {
                                      "type": "boolean"
                                    },
                                    "quizzes": {
                                      "type": "array",
                                      "items": [
                                        {
                                          "type": "object",
                                          "properties": {
                                            "id": {
                                              
                                            },
                                            "viewerRelated": {
                                              "type": "object",
                                              "properties": {
                                                "isCompleted": {
                                                  "type": "boolean"
                                                }
                                              },
                                              "required": [
                                                "isCompleted"
                                              ]
                                            }
                                          },
                                          "required": [
                                            "id",
                                            "viewerRelated"
                                          ]
                                        }
                                      ]
                                    }
                                  },
                                  "required": [
                                    "id",
                                    "name",
                                    "isCompleted",
                                    "quizzes"
                                  ]
                                }
                              ]
                            }
                          },
                          "required": [
                            "id",
                            "name",
                            "finalAssessment",
                            "subLessons"
                          ]
                        }
                      ]
                    }
                  },
                  "required": [
                    "id",
                    "name",
                    "lessons"
                  ]
                },
                {
                  "type": "object",
                  "properties": {
                    "id": {
                      
                    },
                    "name": {
                      
                    },
                    "lessons": {
                      "type": "array",
                      "items": [
                        {
                          "type": "object",
                          "properties": {
                            "id": {
                              
                            },
                            "name": {
                              
                            },
                            "finalAssessment": {
                              
                            },
                            "subLessons": {
                              "type": "array",
                              "items": [
                                {
                                  "type": "object",
                                  "properties": {
                                    "id": {
                                      
                                    },
                                    "name": {
                                      
                                    },
                                    "isCompleted": {
                                      "type": "boolean"
                                    },
                                    "quizzes": {
                                      "type": "array",
                                      "items": [
                                        {
                                          "type": "object",
                                          "properties": {
                                            "id": {
                                              
                                            },
                                            "viewerRelated": {
                                              "type": "object",
                                              "properties": {
                                                "isCompleted": {
                                                  "type": "boolean"
                                                }
                                              },
                                              "required": [
                                                "isCompleted"
                                              ]
                                            }
                                          },
                                          "required": [
                                            "id",
                                            "viewerRelated"
                                          ]
                                        }
                                      ]
                                    }
                                  },
                                  "required": [
                                    "id",
                                    "name",
                                    "isCompleted",
                                    "quizzes"
                                  ]
                                },
                                {
                                  "type": "object",
                                  "properties": {
                                    "id": {
                                      
                                    },
                                    "name": {
                                      
                                    },
                                    "isCompleted": {
                                      "type": "boolean"
                                    },
                                    "quizzes": {
                                      "type": "array",
                                      "items": [
                                        {
                                          "type": "object",
                                          "properties": {
                                            "id": {
                                              
                                            },
                                            "viewerRelated": {
                                              "type": "object",
                                              "properties": {
                                                "isCompleted": {
                                                  "type": "boolean"
                                                }
                                              },
                                              "required": [
                                                "isCompleted"
                                              ]
                                            }
                                          },
                                          "required": [
                                            "id",
                                            "viewerRelated"
                                          ]
                                        }
                                      ]
                                    }
                                  },
                                  "required": [
                                    "id",
                                    "name",
                                    "isCompleted",
                                    "quizzes"
                                  ]
                                }
                              ]
                            }
                          },
                          "required": [
                            "id",
                            "name",
                            "finalAssessment",
                            "subLessons"
                          ]
                        },
                        {
                          "type": "object",
                          "properties": {
                            "id": {
                              
                            },
                            "name": {
                              
                            },
                            "finalAssessment": {
                              
                            },
                            "subLessons": {
                              "type": "array",
                              "items": [
                                {
                                  "type": "object",
                                  "properties": {
                                    "id": {
                                      
                                    },
                                    "name": {
                                      
                                    },
                                    "isCompleted": {
                                      "type": "boolean"
                                    },
                                    "quizzes": {
                                      "type": "array",
                                      "items": [
                                        {
                                          "type": "object",
                                          "properties": {
                                            "id": {
                                              
                                            },
                                            "viewerRelated": {
                                              "type": "object",
                                              "properties": {
                                                "isCompleted": {
                                                  "type": "boolean"
                                                }
                                              },
                                              "required": [
                                                "isCompleted"
                                              ]
                                            }
                                          },
                                          "required": [
                                            "id",
                                            "viewerRelated"
                                          ]
                                        }
                                      ]
                                    }
                                  },
                                  "required": [
                                    "id",
                                    "name",
                                    "isCompleted",
                                    "quizzes"
                                  ]
                                },
                                {
                                  "type": "object",
                                  "properties": {
                                    "id": {
                                      
                                    },
                                    "name": {
                                      
                                    },
                                    "isCompleted": {
                                      "type": "boolean"
                                    },
                                    "quizzes": {
                                      "type": "array",
                                      "items": [
                                        {
                                          "type": "object",
                                          "properties": {
                                            "id": {
                                              
                                            },
                                            "viewerRelated": {
                                              "type": "object",
                                              "properties": {
                                                "isCompleted": {
                                                  "type": "boolean"
                                                }
                                              },
                                              "required": [
                                                "isCompleted"
                                              ]
                                            }
                                          },
                                          "required": [
                                            "id",
                                            "viewerRelated"
                                          ]
                                        }
                                      ]
                                    }
                                  },
                                  "required": [
                                    "id",
                                    "name",
                                    "isCompleted",
                                    "quizzes"
                                  ]
                                },
                                {
                                  "type": "object",
                                  "properties": {
                                    "id": {
                                      
                                    },
                                    "name": {
                                      
                                    },
                                    "isCompleted": {
                                      "type": "boolean"
                                    },
                                    "quizzes": {
                                      "type": "array",
                                      "items": [
                                        {
                                          "type": "object",
                                          "properties": {
                                            "id": {
                                              
                                            },
                                            "viewerRelated": {
                                              "type": "object",
                                              "properties": {
                                                "isCompleted": {
                                                  "type": "boolean"
                                                }
                                              },
                                              "required": [
                                                "isCompleted"
                                              ]
                                            }
                                          },
                                          "required": [
                                            "id",
                                            "viewerRelated"
                                          ]
                                        }
                                      ]
                                    }
                                  },
                                  "required": [
                                    "id",
                                    "name",
                                    "isCompleted",
                                    "quizzes"
                                  ]
                                }
                              ]
                            }
                          },
                          "required": [
                            "id",
                            "name",
                            "finalAssessment",
                            "subLessons"
                          ]
                        },
                        {
                          "type": "object",
                          "properties": {
                            "id": {
                              
                            },
                            "name": {
                              
                            },
                            "finalAssessment": {
                              
                            },
                            "subLessons": {
                              "type": "array",
                              "items": [
                                {
                                  "type": "object",
                                  "properties": {
                                    "id": {
                                      
                                    },
                                    "name": {
                                      
                                    },
                                    "isCompleted": {
                                      "type": "boolean"
                                    },
                                    "quizzes": {
                                      "type": "array",
                                      "items": [
                                        {
                                          "type": "object",
                                          "properties": {
                                            "id": {
                                              
                                            },
                                            "viewerRelated": {
                                              "type": "object",
                                              "properties": {
                                                "isCompleted": {
                                                  "type": "boolean"
                                                }
                                              },
                                              "required": [
                                                "isCompleted"
                                              ]
                                            }
                                          },
                                          "required": [
                                            "id",
                                            "viewerRelated"
                                          ]
                                        }
                                      ]
                                    }
                                  },
                                  "required": [
                                    "id",
                                    "name",
                                    "isCompleted",
                                    "quizzes"
                                  ]
                                },
                                {
                                  "type": "object",
                                  "properties": {
                                    "id": {
                                      
                                    },
                                    "name": {
                                      
                                    },
                                    "isCompleted": {
                                      "type": "boolean"
                                    },
                                    "quizzes": {
                                      "type": "array",
                                      "items": [
                                        {
                                          "type": "object",
                                          "properties": {
                                            "id": {
                                              
                                            },
                                            "viewerRelated": {
                                              "type": "object",
                                              "properties": {
                                                "isCompleted": {
                                                  "type": "boolean"
                                                }
                                              },
                                              "required": [
                                                "isCompleted"
                                              ]
                                            }
                                          },
                                          "required": [
                                            "id",
                                            "viewerRelated"
                                          ]
                                        }
                                      ]
                                    }
                                  },
                                  "required": [
                                    "id",
                                    "name",
                                    "isCompleted",
                                    "quizzes"
                                  ]
                                },
                                {
                                  "type": "object",
                                  "properties": {
                                    "id": {
                                      
                                    },
                                    "name": {
                                      
                                    },
                                    "isCompleted": {
                                      "type": "boolean"
                                    },
                                    "quizzes": {
                                      "type": "array",
                                      "items": [
                                        {
                                          "type": "object",
                                          "properties": {
                                            "id": {
                                              
                                            },
                                            "viewerRelated": {
                                              "type": "object",
                                              "properties": {
                                                "isCompleted": {
                                                  "type": "boolean"
                                                }
                                              },
                                              "required": [
                                                "isCompleted"
                                              ]
                                            }
                                          },
                                          "required": [
                                            "id",
                                            "viewerRelated"
                                          ]
                                        }
                                      ]
                                    }
                                  },
                                  "required": [
                                    "id",
                                    "name",
                                    "isCompleted",
                                    "quizzes"
                                  ]
                                }
                              ]
                            }
                          },
                          "required": [
                            "id",
                            "name",
                            "finalAssessment",
                            "subLessons"
                          ]
                        }
                      ]
                    }
                  },
                  "required": [
                    "id",
                    "name",
                    "lessons"
                  ]
                },
                {
                  "type": "object",
                  "properties": {
                    "id": {
                      
                    },
                    "name": {
                      
                    },
                    "lessons": {
                      "type": "array",
                      "items": [
                        {
                          "type": "object",
                          "properties": {
                            "id": {
                              
                            },
                            "name": {
                              
                            },
                            "finalAssessment": {
                              
                            },
                            "subLessons": {
                              "type": "array",
                              "items": [
                                {
                                  "type": "object",
                                  "properties": {
                                    "id": {
                                      
                                    },
                                    "name": {
                                      
                                    },
                                    "isCompleted": {
                                      "type": "boolean"
                                    },
                                    "quizzes": {
                                      "type": "array",
                                      "items": [
                                        {
                                          "type": "object",
                                          "properties": {
                                            "id": {
                                              
                                            },
                                            "viewerRelated": {
                                              "type": "object",
                                              "properties": {
                                                "isCompleted": {
                                                  "type": "boolean"
                                                }
                                              },
                                              "required": [
                                                "isCompleted"
                                              ]
                                            }
                                          },
                                          "required": [
                                            "id",
                                            "viewerRelated"
                                          ]
                                        }
                                      ]
                                    }
                                  },
                                  "required": [
                                    "id",
                                    "name",
                                    "isCompleted",
                                    "quizzes"
                                  ]
                                },
                                {
                                  "type": "object",
                                  "properties": {
                                    "id": {
                                      
                                    },
                                    "name": {
                                      
                                    },
                                    "isCompleted": {
                                      "type": "boolean"
                                    },
                                    "quizzes": {
                                      "type": "array",
                                      "items": [
                                        {
                                          "type": "object",
                                          "properties": {
                                            "id": {
                                              
                                            },
                                            "viewerRelated": {
                                              "type": "object",
                                              "properties": {
                                                "isCompleted": {
                                                  "type": "boolean"
                                                }
                                              },
                                              "required": [
                                                "isCompleted"
                                              ]
                                            }
                                          },
                                          "required": [
                                            "id",
                                            "viewerRelated"
                                          ]
                                        }
                                      ]
                                    }
                                  },
                                  "required": [
                                    "id",
                                    "name",
                                    "isCompleted",
                                    "quizzes"
                                  ]
                                },
                                {
                                  "type": "object",
                                  "properties": {
                                    "id": {
                                      
                                    },
                                    "name": {
                                      
                                    },
                                    "isCompleted": {
                                      "type": "boolean"
                                    },
                                    "quizzes": {
                                      "type": "array",
                                      "items": [
                                        {
                                          "type": "object",
                                          "properties": {
                                            "id": {
                                              
                                            },
                                            "viewerRelated": {
                                              "type": "object",
                                              "properties": {
                                                "isCompleted": {
                                                  "type": "boolean"
                                                }
                                              },
                                              "required": [
                                                "isCompleted"
                                              ]
                                            }
                                          },
                                          "required": [
                                            "id",
                                            "viewerRelated"
                                          ]
                                        }
                                      ]
                                    }
                                  },
                                  "required": [
                                    "id",
                                    "name",
                                    "isCompleted",
                                    "quizzes"
                                  ]
                                }
                              ]
                            }
                          },
                          "required": [
                            "id",
                            "name",
                            "finalAssessment",
                            "subLessons"
                          ]
                        },
                        {
                          "type": "object",
                          "properties": {
                            "id": {
                              
                            },
                            "name": {
                              
                            },
                            "finalAssessment": {
                              
                            },
                            "subLessons": {
                              "type": "array",
                              "items": [
                                {
                                  "type": "object",
                                  "properties": {
                                    "id": {
                                      
                                    },
                                    "name": {
                                      
                                    },
                                    "isCompleted": {
                                      "type": "boolean"
                                    },
                                    "quizzes": {
                                      "type": "array",
                                      "items": [
                                        {
                                          "type": "object",
                                          "properties": {
                                            "id": {
                                              
                                            },
                                            "viewerRelated": {
                                              "type": "object",
                                              "properties": {
                                                "isCompleted": {
                                                  "type": "boolean"
                                                }
                                              },
                                              "required": [
                                                "isCompleted"
                                              ]
                                            }
                                          },
                                          "required": [
                                            "id",
                                            "viewerRelated"
                                          ]
                                        }
                                      ]
                                    }
                                  },
                                  "required": [
                                    "id",
                                    "name",
                                    "isCompleted",
                                    "quizzes"
                                  ]
                                },
                                {
                                  "type": "object",
                                  "properties": {
                                    "id": {
                                      
                                    },
                                    "name": {
                                      
                                    },
                                    "isCompleted": {
                                      "type": "boolean"
                                    },
                                    "quizzes": {
                                      "type": "array",
                                      "items": [
                                        {
                                          "type": "object",
                                          "properties": {
                                            "id": {
                                              
                                            },
                                            "viewerRelated": {
                                              "type": "object",
                                              "properties": {
                                                "isCompleted": {
                                                  "type": "boolean"
                                                }
                                              },
                                              "required": [
                                                "isCompleted"
                                              ]
                                            }
                                          },
                                          "required": [
                                            "id",
                                            "viewerRelated"
                                          ]
                                        }
                                      ]
                                    }
                                  },
                                  "required": [
                                    "id",
                                    "name",
                                    "isCompleted",
                                    "quizzes"
                                  ]
                                },
                                {
                                  "type": "object",
                                  "properties": {
                                    "id": {
                                      
                                    },
                                    "name": {
                                      
                                    },
                                    "isCompleted": {
                                      "type": "boolean"
                                    },
                                    "quizzes": {
                                      "type": "array",
                                      "items": [
                                        {
                                          "type": "object",
                                          "properties": {
                                            "id": {
                                              
                                            },
                                            "viewerRelated": {
                                              "type": "object",
                                              "properties": {
                                                "isCompleted": {
                                                  "type": "boolean"
                                                }
                                              },
                                              "required": [
                                                "isCompleted"
                                              ]
                                            }
                                          },
                                          "required": [
                                            "id",
                                            "viewerRelated"
                                          ]
                                        }
                                      ]
                                    }
                                  },
                                  "required": [
                                    "id",
                                    "name",
                                    "isCompleted",
                                    "quizzes"
                                  ]
                                }
                              ]
                            }
                          },
                          "required": [
                            "id",
                            "name",
                            "finalAssessment",
                            "subLessons"
                          ]
                        },
                        {
                          "type": "object",
                          "properties": {
                            "id": {
                              
                            },
                            "name": {
                              
                            },
                            "finalAssessment": {
                              
                            },
                            "subLessons": {
                              "type": "array",
                              "items": [
                                {
                                  "type": "object",
                                  "properties": {
                                    "id": {
                                      
                                    },
                                    "name": {
                                      
                                    },
                                    "isCompleted": {
                                      "type": "boolean"
                                    },
                                    "quizzes": {
                                      "type": "array",
                                      "items": [
                                        {
                                          "type": "object",
                                          "properties": {
                                            "id": {
                                              
                                            },
                                            "viewerRelated": {
                                              "type": "object",
                                              "properties": {
                                                "isCompleted": {
                                                  "type": "boolean"
                                                }
                                              },
                                              "required": [
                                                "isCompleted"
                                              ]
                                            }
                                          },
                                          "required": [
                                            "id",
                                            "viewerRelated"
                                          ]
                                        }
                                      ]
                                    }
                                  },
                                  "required": [
                                    "id",
                                    "name",
                                    "isCompleted",
                                    "quizzes"
                                  ]
                                },
                                {
                                  "type": "object",
                                  "properties": {
                                    "id": {
                                      
                                    },
                                    "name": {
                                      
                                    },
                                    "isCompleted": {
                                      "type": "boolean"
                                    },
                                    "quizzes": {
                                      "type": "array",
                                      "items": [
                                        {
                                          "type": "object",
                                          "properties": {
                                            "id": {
                                              
                                            },
                                            "viewerRelated": {
                                              "type": "object",
                                              "properties": {
                                                "isCompleted": {
                                                  "type": "boolean"
                                                }
                                              },
                                              "required": [
                                                "isCompleted"
                                              ]
                                            }
                                          },
                                          "required": [
                                            "id",
                                            "viewerRelated"
                                          ]
                                        }
                                      ]
                                    }
                                  },
                                  "required": [
                                    "id",
                                    "name",
                                    "isCompleted",
                                    "quizzes"
                                  ]
                                }
                              ]
                            }
                          },
                          "required": [
                            "id",
                            "name",
                            "finalAssessment",
                            "subLessons"
                          ]
                        }
                      ]
                    }
                  },
                  "required": [
                    "id",
                    "name",
                    "lessons"
                  ]
                },
                {
                  "type": "object",
                  "properties": {
                    "id": {
                      
                    },
                    "name": {
                      
                    },
                    "lessons": {
                      "type": "array",
                      "items": [
                        {
                          "type": "object",
                          "properties": {
                            "id": {
                              
                            },
                            "name": {
                              
                            },
                            "finalAssessment": {
                              
                            },
                            "subLessons": {
                              "type": "array",
                              "items": [
                                {
                                  "type": "object",
                                  "properties": {
                                    "id": {
                                      
                                    },
                                    "name": {
                                      
                                    },
                                    "isCompleted": {
                                      "type": "boolean"
                                    },
                                    "quizzes": {
                                      "type": "array",
                                      "items": [
                                        {
                                          "type": "object",
                                          "properties": {
                                            "id": {
                                              
                                            },
                                            "viewerRelated": {
                                              "type": "object",
                                              "properties": {
                                                "isCompleted": {
                                                  "type": "boolean"
                                                }
                                              },
                                              "required": [
                                                "isCompleted"
                                              ]
                                            }
                                          },
                                          "required": [
                                            "id",
                                            "viewerRelated"
                                          ]
                                        }
                                      ]
                                    }
                                  },
                                  "required": [
                                    "id",
                                    "name",
                                    "isCompleted",
                                    "quizzes"
                                  ]
                                },
                                {
                                  "type": "object",
                                  "properties": {
                                    "id": {
                                      
                                    },
                                    "name": {
                                      
                                    },
                                    "isCompleted": {
                                      "type": "boolean"
                                    },
                                    "quizzes": {
                                      "type": "array",
                                      "items": [
                                        {
                                          "type": "object",
                                          "properties": {
                                            "id": {
                                              
                                            },
                                            "viewerRelated": {
                                              "type": "object",
                                              "properties": {
                                                "isCompleted": {
                                                  "type": "boolean"
                                                }
                                              },
                                              "required": [
                                                "isCompleted"
                                              ]
                                            }
                                          },
                                          "required": [
                                            "id",
                                            "viewerRelated"
                                          ]
                                        }
                                      ]
                                    }
                                  },
                                  "required": [
                                    "id",
                                    "name",
                                    "isCompleted",
                                    "quizzes"
                                  ]
                                },
                                {
                                  "type": "object",
                                  "properties": {
                                    "id": {
                                      
                                    },
                                    "name": {
                                      
                                    },
                                    "isCompleted": {
                                      "type": "boolean"
                                    },
                                    "quizzes": {
                                      "type": "array",
                                      "items": [
                                        {
                                          "type": "object",
                                          "properties": {
                                            "id": {
                                              
                                            },
                                            "viewerRelated": {
                                              "type": "object",
                                              "properties": {
                                                "isCompleted": {
                                                  "type": "boolean"
                                                }
                                              },
                                              "required": [
                                                "isCompleted"
                                              ]
                                            }
                                          },
                                          "required": [
                                            "id",
                                            "viewerRelated"
                                          ]
                                        }
                                      ]
                                    }
                                  },
                                  "required": [
                                    "id",
                                    "name",
                                    "isCompleted",
                                    "quizzes"
                                  ]
                                }
                              ]
                            }
                          },
                          "required": [
                            "id",
                            "name",
                            "finalAssessment",
                            "subLessons"
                          ]
                        },
                        {
                          "type": "object",
                          "properties": {
                            "id": {
                              
                            },
                            "name": {
                              
                            },
                            "finalAssessment": {
                              
                            },
                            "subLessons": {
                              "type": "array",
                              "items": [
                                {
                                  "type": "object",
                                  "properties": {
                                    "id": {
                                      
                                    },
                                    "name": {
                                      
                                    },
                                    "isCompleted": {
                                      "type": "boolean"
                                    },
                                    "quizzes": {
                                      "type": "array",
                                      "items": [
                                        {
                                          "type": "object",
                                          "properties": {
                                            "id": {
                                              
                                            },
                                            "viewerRelated": {
                                              "type": "object",
                                              "properties": {
                                                "isCompleted": {
                                                  "type": "boolean"
                                                }
                                              },
                                              "required": [
                                                "isCompleted"
                                              ]
                                            }
                                          },
                                          "required": [
                                            "id",
                                            "viewerRelated"
                                          ]
                                        }
                                      ]
                                    }
                                  },
                                  "required": [
                                    "id",
                                    "name",
                                    "isCompleted",
                                    "quizzes"
                                  ]
                                },
                                {
                                  "type": "object",
                                  "properties": {
                                    "id": {
                                      
                                    },
                                    "name": {
                                      
                                    },
                                    "isCompleted": {
                                      "type": "boolean"
                                    },
                                    "quizzes": {
                                      "type": "array",
                                      "items": [
                                        {
                                          "type": "object",
                                          "properties": {
                                            "id": {
                                              
                                            },
                                            "viewerRelated": {
                                              "type": "object",
                                              "properties": {
                                                "isCompleted": {
                                                  "type": "boolean"
                                                }
                                              },
                                              "required": [
                                                "isCompleted"
                                              ]
                                            }
                                          },
                                          "required": [
                                            "id",
                                            "viewerRelated"
                                          ]
                                        }
                                      ]
                                    }
                                  },
                                  "required": [
                                    "id",
                                    "name",
                                    "isCompleted",
                                    "quizzes"
                                  ]
                                },
                                {
                                  "type": "object",
                                  "properties": {
                                    "id": {
                                      
                                    },
                                    "name": {
                                      
                                    },
                                    "isCompleted": {
                                      "type": "boolean"
                                    },
                                    "quizzes": {
                                      "type": "array",
                                      "items": [
                                        {
                                          "type": "object",
                                          "properties": {
                                            "id": {
                                              
                                            },
                                            "viewerRelated": {
                                              "type": "object",
                                              "properties": {
                                                "isCompleted": {
                                                  "type": "boolean"
                                                }
                                              },
                                              "required": [
                                                "isCompleted"
                                              ]
                                            }
                                          },
                                          "required": [
                                            "id",
                                            "viewerRelated"
                                          ]
                                        }
                                      ]
                                    }
                                  },
                                  "required": [
                                    "id",
                                    "name",
                                    "isCompleted",
                                    "quizzes"
                                  ]
                                }
                              ]
                            }
                          },
                          "required": [
                            "id",
                            "name",
                            "finalAssessment",
                            "subLessons"
                          ]
                        },
                        {
                          "type": "object",
                          "properties": {
                            "id": {
                              
                            },
                            "name": {
                              
                            },
                            "finalAssessment": {
                              
                            },
                            "subLessons": {
                              "type": "array",
                              "items": [
                                {
                                  "type": "object",
                                  "properties": {
                                    "id": {
                                      
                                    },
                                    "name": {
                                      
                                    },
                                    "isCompleted": {
                                      "type": "boolean"
                                    },
                                    "quizzes": {
                                      "type": "array",
                                      "items": [
                                        {
                                          "type": "object",
                                          "properties": {
                                            "id": {
                                              
                                            },
                                            "viewerRelated": {
                                              "type": "object",
                                              "properties": {
                                                "isCompleted": {
                                                  "type": "boolean"
                                                }
                                              },
                                              "required": [
                                                "isCompleted"
                                              ]
                                            }
                                          },
                                          "required": [
                                            "id",
                                            "viewerRelated"
                                          ]
                                        }
                                      ]
                                    }
                                  },
                                  "required": [
                                    "id",
                                    "name",
                                    "isCompleted",
                                    "quizzes"
                                  ]
                                },
                                {
                                  "type": "object",
                                  "properties": {
                                    "id": {
                                      
                                    },
                                    "name": {
                                      
                                    },
                                    "isCompleted": {
                                      "type": "boolean"
                                    },
                                    "quizzes": {
                                      "type": "array",
                                      "items": [
                                        {
                                          "type": "object",
                                          "properties": {
                                            "id": {
                                              
                                            },
                                            "viewerRelated": {
                                              "type": "object",
                                              "properties": {
                                                "isCompleted": {
                                                  "type": "boolean"
                                                }
                                              },
                                              "required": [
                                                "isCompleted"
                                              ]
                                            }
                                          },
                                          "required": [
                                            "id",
                                            "viewerRelated"
                                          ]
                                        }
                                      ]
                                    }
                                  },
                                  "required": [
                                    "id",
                                    "name",
                                    "isCompleted",
                                    "quizzes"
                                  ]
                                }
                              ]
                            }
                          },
                          "required": [
                            "id",
                            "name",
                            "finalAssessment",
                            "subLessons"
                          ]
                        }
                      ]
                    }
                  },
                  "required": [
                    "id",
                    "name",
                    "lessons"
                  ]
                }
              ]
            }
          },
          "required": [
            "sections"
          ]
        }
      },
      "required": [
        "viewer"
      ]
    }
  },
  "required": [
    "data"
  ]
}

QUIZ_DETALE = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "data": {
      "type": "object",
      "properties": {
        "node": {
          "type": "object",
          "properties": {
            "__typename": {
              
            },
            "name": {
              
            },
            "type": {
              
            },
            "questions": {
              "type": "array",
              "items": [
                {
                  "type": "object",
                  "properties": {
                    "id": {
                      
                    },
                    "questionType": {
                      
                    },
                    "text": {
                      "type": "object",
                      "properties": {
                        "id": {
                          
                        },
                        "content": {
                          
                        }
                      },
                      "required": [
                        "id",
                        "content"
                      ]
                    },
                    "note": {
                      "type": "object",
                      "properties": {
                        "id": {
                          
                        },
                        "rightNote": {
                          
                        },
                        "wrongNote": {
                          
                        }
                      },
                      "required": [
                        "id",
                        "rightNote",
                        "wrongNote"
                      ]
                    },
                    "answers": {
                      "type": "array",
                      "items": [
                        {
                          "type": "object",
                          "properties": {
                            "id": {
                              
                            },
                            "text": {
                              
                            },
                            "isRightAnswer": {
                              "type": "boolean"
                            }
                          },
                          "required": [
                            "id",
                            "text",
                            "isRightAnswer"
                          ]
                        },
                        {
                          "type": "object",
                          "properties": {
                            "id": {
                              
                            },
                            "text": {
                              
                            },
                            "isRightAnswer": {
                              "type": "boolean"
                            }
                          },
                          "required": [
                            "id",
                            "text",
                            "isRightAnswer"
                          ]
                        },
                        {
                          "type": "object",
                          "properties": {
                            "id": {
                              
                            },
                            "text": {
                              
                            },
                            "isRightAnswer": {
                              "type": "boolean"
                            }
                          },
                          "required": [
                            "id",
                            "text",
                            "isRightAnswer"
                          ]
                        },
                        {
                          "type": "object",
                          "properties": {
                            "id": {
                              
                            },
                            "text": {
                              
                            },
                            "isRightAnswer": {
                              "type": "boolean"
                            }
                          },
                          "required": [
                            "id",
                            "text",
                            "isRightAnswer"
                          ]
                        }
                      ]
                    }
                  },
                  "required": [
                    "id",
                    "questionType",
                    "text",
                    "note",
                    "answers"
                  ]
                },
                {
                  "type": "object",
                  "properties": {
                    "id": {
                      
                    },
                    "questionType": {
                      
                    },
                    "text": {
                      "type": "object",
                      "properties": {
                        "id": {
                          
                        },
                        "content": {
                          
                        }
                      },
                      "required": [
                        "id",
                        "content"
                      ]
                    },
                    "note": {
                      "type": "object",
                      "properties": {
                        "id": {
                          
                        },
                        "rightNote": {
                          
                        },
                        "wrongNote": {
                          
                        }
                      },
                      "required": [
                        "id",
                        "rightNote",
                        "wrongNote"
                      ]
                    },
                    "answers": {
                      "type": "array",
                      "items": [
                        {
                          "type": "object",
                          "properties": {
                            "id": {
                              
                            },
                            "text": {
                              
                            },
                            "isRightAnswer": {
                              "type": "boolean"
                            }
                          },
                          "required": [
                            "id",
                            "text",
                            "isRightAnswer"
                          ]
                        },
                        {
                          "type": "object",
                          "properties": {
                            "id": {
                              
                            },
                            "text": {
                              
                            },
                            "isRightAnswer": {
                              "type": "boolean"
                            }
                          },
                          "required": [
                            "id",
                            "text",
                            "isRightAnswer"
                          ]
                        }
                      ]
                    }
                  },
                  "required": [
                    "id",
                    "questionType",
                    "text",
                    "note",
                    "answers"
                  ]
                },
                {
                  "type": "object",
                  "properties": {
                    "id": {
                      
                    },
                    "questionType": {
                      
                    },
                    "text": {
                      "type": "object",
                      "properties": {
                        "id": {
                          
                        },
                        "content": {
                          
                        }
                      },
                      "required": [
                        "id",
                        "content"
                      ]
                    },
                    "note": {
                      "type": "object",
                      "properties": {
                        "id": {
                          
                        },
                        "rightNote": {
                          
                        },
                        "wrongNote": {
                          
                        }
                      },
                      "required": [
                        "id",
                        "rightNote",
                        "wrongNote"
                      ]
                    },
                    "answers": {
                      "type": "array",
                      "items": [
                        {
                          "type": "object",
                          "properties": {
                            "id": {
                              
                            },
                            "text": {
                              
                            },
                            "isRightAnswer": {
                              "type": "boolean"
                            }
                          },
                          "required": [
                            "id",
                            "text",
                            "isRightAnswer"
                          ]
                        },
                        {
                          "type": "object",
                          "properties": {
                            "id": {
                              
                            },
                            "text": {
                              
                            },
                            "isRightAnswer": {
                              "type": "boolean"
                            }
                          },
                          "required": [
                            "id",
                            "text",
                            "isRightAnswer"
                          ]
                        },
                        {
                          "type": "object",
                          "properties": {
                            "id": {
                              
                            },
                            "text": {
                              
                            },
                            "isRightAnswer": {
                              "type": "boolean"
                            }
                          },
                          "required": [
                            "id",
                            "text",
                            "isRightAnswer"
                          ]
                        },
                        {
                          "type": "object",
                          "properties": {
                            "id": {
                              
                            },
                            "text": {
                              
                            },
                            "isRightAnswer": {
                              "type": "boolean"
                            }
                          },
                          "required": [
                            "id",
                            "text",
                            "isRightAnswer"
                          ]
                        }
                      ]
                    }
                  },
                  "required": [
                    "id",
                    "questionType",
                    "text",
                    "note",
                    "answers"
                  ]
                },
                {
                  "type": "object",
                  "properties": {
                    "id": {
                      
                    },
                    "questionType": {
                      
                    },
                    "text": {
                      "type": "object",
                      "properties": {
                        "id": {
                          
                        },
                        "content": {
                          
                        }
                      },
                      "required": [
                        "id",
                        "content"
                      ]
                    },
                    "note": {
                      "type": "object",
                      "properties": {
                        "id": {
                          
                        },
                        "rightNote": {
                          
                        },
                        "wrongNote": {
                          
                        }
                      },
                      "required": [
                        "id",
                        "rightNote",
                        "wrongNote"
                      ]
                    },
                    "answers": {
                      "type": "array",
                      "items": [
                        {
                          "type": "object",
                          "properties": {
                            "id": {
                              
                            },
                            "text": {
                              
                            },
                            "isRightAnswer": {
                              "type": "boolean"
                            }
                          },
                          "required": [
                            "id",
                            "text",
                            "isRightAnswer"
                          ]
                        },
                        {
                          "type": "object",
                          "properties": {
                            "id": {
                              
                            },
                            "text": {
                              
                            },
                            "isRightAnswer": {
                              "type": "boolean"
                            }
                          },
                          "required": [
                            "id",
                            "text",
                            "isRightAnswer"
                          ]
                        },
                        {
                          "type": "object",
                          "properties": {
                            "id": {
                              
                            },
                            "text": {
                              
                            },
                            "isRightAnswer": {
                              "type": "boolean"
                            }
                          },
                          "required": [
                            "id",
                            "text",
                            "isRightAnswer"
                          ]
                        },
                        {
                          "type": "object",
                          "properties": {
                            "id": {
                              
                            },
                            "text": {
                              
                            },
                            "isRightAnswer": {
                              "type": "boolean"
                            }
                          },
                          "required": [
                            "id",
                            "text",
                            "isRightAnswer"
                          ]
                        }
                      ]
                    }
                  },
                  "required": [
                    "id",
                    "questionType",
                    "text",
                    "note",
                    "answers"
                  ]
                },
                {
                  "type": "object",
                  "properties": {
                    "id": {
                      
                    },
                    "questionType": {
                      
                    },
                    "text": {
                      "type": "object",
                      "properties": {
                        "id": {
                          
                        },
                        "content": {
                          
                        }
                      },
                      "required": [
                        "id",
                        "content"
                      ]
                    },
                    "note": {
                      "type": "object",
                      "properties": {
                        "id": {
                          
                        },
                        "rightNote": {
                          
                        },
                        "wrongNote": {
                          
                        }
                      },
                      "required": [
                        "id",
                        "rightNote",
                        "wrongNote"
                      ]
                    },
                    "answers": {
                      "type": "array",
                      "items": [
                        {
                          "type": "object",
                          "properties": {
                            "id": {
                              
                            },
                            "text": {
                              
                            },
                            "isRightAnswer": {
                              "type": "boolean"
                            }
                          },
                          "required": [
                            "id",
                            "text",
                            "isRightAnswer"
                          ]
                        },
                        {
                          "type": "object",
                          "properties": {
                            "id": {
                              
                            },
                            "text": {
                              
                            },
                            "isRightAnswer": {
                              "type": "boolean"
                            }
                          },
                          "required": [
                            "id",
                            "text",
                            "isRightAnswer"
                          ]
                        },
                        {
                          "type": "object",
                          "properties": {
                            "id": {
                              
                            },
                            "text": {
                              
                            },
                            "isRightAnswer": {
                              "type": "boolean"
                            }
                          },
                          "required": [
                            "id",
                            "text",
                            "isRightAnswer"
                          ]
                        },
                        {
                          "type": "object",
                          "properties": {
                            "id": {
                              
                            },
                            "text": {
                              
                            },
                            "isRightAnswer": {
                              "type": "boolean"
                            }
                          },
                          "required": [
                            "id",
                            "text",
                            "isRightAnswer"
                          ]
                        }
                      ]
                    }
                  },
                  "required": [
                    "id",
                    "questionType",
                    "text",
                    "note",
                    "answers"
                  ]
                }
              ]
            }
          },
          "required": [
            "__typename",
            "name",
            "type",
            "questions"
          ]
        }
      },
      "required": [
        "node"
      ]
    }
  },
  "required": [
    "data"
  ]
}

QUIZ_STAT = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "data": {
      "type": "object",
      "properties": {
        "viewer": {
          "type": "object",
          "properties": {
            "profile": {
              "type": "object",
              "properties": {
                "statistics": {
                  "type": "object",
                  "properties": {
                    "percQuestionsAnsweredOnFirstTry": {
                      "type": "integer"
                    }
                  },
                  "required": [
                    "percQuestionsAnsweredOnFirstTry"
                  ]
                }
              },
              "required": [
                "statistics"
              ]
            }
          },
          "required": [
            "profile"
          ]
        }
      },
      "required": [
        "viewer"
      ]
    }
  },
  "required": [
    "data"
  ]
}

ONBORDING_PHOTO = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "data": {
      "type": "object",
      "properties": {
        "viewer": {
          "type": "object",
          "properties": {
            "onboardingImages": {
              "type": "array",
              "items": [
                {
                  "type": "object",
                  "properties": {
                    "questionId": {
                      "type": "string"
                    },
                    "url": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "questionId",
                    "url"
                  ]
                }
              ]
            }
          },
          "required": [
            "onboardingImages"
          ]
        }
      },
      "required": [
        "viewer"
      ]
    }
  },
  "required": [
    "data"
  ]
}

ONBOARDING_QUESTIONS = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "data": {
      "type": "object",
      "properties": {
        "viewer": {
          "type": "object",
          "properties": {
            "onboardingQuestions": {
              "type": "array",
              "items": [
                {
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "string"
                    },
                    "text": {
                      "type": "string"
                    },
                    "title": {
                      "type": "string"
                    },
                    "section": {
                      "type": "string"
                    },
                    "note": {
                      "type": "string"
                    },
                    "answers": {
                      "type": "array",
                      "items": [
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "string"
                            },
                            "picture": {
                              "type": "string"
                            },
                            "emoji": {
                              "type": "null"
                            },
                            "alignment": {
                              "type": "string"
                            },
                            "eventPropValue": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "text",
                            "picture",
                            "emoji",
                            "alignment",
                            "eventPropValue"
                          ]
                        },
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "string"
                            },
                            "picture": {
                              "type": "string"
                            },
                            "emoji": {
                              "type": "null"
                            },
                            "alignment": {
                              "type": "string"
                            },
                            "eventPropValue": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "text",
                            "picture",
                            "emoji",
                            "alignment",
                            "eventPropValue"
                          ]
                        }
                      ]
                    },
                    "subQuestions": {
                      "type": "array",
                      "items": {}
                    }
                  },
                  "required": [
                    "id",
                    "text",
                    "title",
                    "section",
                    "note",
                    "answers",
                    "subQuestions"
                  ]
                },
                {
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "string"
                    },
                    "text": {
                      "type": "string"
                    },
                    "title": {
                      "type": "string"
                    },
                    "section": {
                      "type": "string"
                    },
                    "note": {
                      "type": "null"
                    },
                    "answers": {
                      "type": "array",
                      "items": [
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "string"
                            },
                            "picture": {
                              "type": "string"
                            },
                            "emoji": {
                              "type": "null"
                            },
                            "alignment": {
                              "type": "string"
                            },
                            "eventPropValue": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "text",
                            "picture",
                            "emoji",
                            "alignment",
                            "eventPropValue"
                          ]
                        },
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "string"
                            },
                            "picture": {
                              "type": "string"
                            },
                            "emoji": {
                              "type": "null"
                            },
                            "alignment": {
                              "type": "string"
                            },
                            "eventPropValue": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "text",
                            "picture",
                            "emoji",
                            "alignment",
                            "eventPropValue"
                          ]
                        },
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "string"
                            },
                            "picture": {
                              "type": "string"
                            },
                            "emoji": {
                              "type": "null"
                            },
                            "alignment": {
                              "type": "string"
                            },
                            "eventPropValue": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "text",
                            "picture",
                            "emoji",
                            "alignment",
                            "eventPropValue"
                          ]
                        },
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "string"
                            },
                            "picture": {
                              "type": "string"
                            },
                            "emoji": {
                              "type": "null"
                            },
                            "alignment": {
                              "type": "string"
                            },
                            "eventPropValue": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "text",
                            "picture",
                            "emoji",
                            "alignment",
                            "eventPropValue"
                          ]
                        },
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "string"
                            },
                            "picture": {
                              "type": "string"
                            },
                            "emoji": {
                              "type": "null"
                            },
                            "alignment": {
                              "type": "string"
                            },
                            "eventPropValue": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "text",
                            "picture",
                            "emoji",
                            "alignment",
                            "eventPropValue"
                          ]
                        },
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "string"
                            },
                            "picture": {
                              "type": "string"
                            },
                            "emoji": {
                              "type": "null"
                            },
                            "alignment": {
                              "type": "string"
                            },
                            "eventPropValue": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "text",
                            "picture",
                            "emoji",
                            "alignment",
                            "eventPropValue"
                          ]
                        },
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "string"
                            },
                            "picture": {
                              "type": "string"
                            },
                            "emoji": {
                              "type": "null"
                            },
                            "alignment": {
                              "type": "string"
                            },
                            "eventPropValue": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "text",
                            "picture",
                            "emoji",
                            "alignment",
                            "eventPropValue"
                          ]
                        },
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "string"
                            },
                            "picture": {
                              "type": "string"
                            },
                            "emoji": {
                              "type": "null"
                            },
                            "alignment": {
                              "type": "string"
                            },
                            "eventPropValue": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "text",
                            "picture",
                            "emoji",
                            "alignment",
                            "eventPropValue"
                          ]
                        }
                      ]
                    },
                    "subQuestions": {
                      "type": "array",
                      "items": {}
                    }
                  },
                  "required": [
                    "id",
                    "text",
                    "title",
                    "section",
                    "note",
                    "answers",
                    "subQuestions"
                  ]
                },
                {
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "string"
                    },
                    "text": {
                      "type": "string"
                    },
                    "title": {
                      "type": "null"
                    },
                    "section": {
                      "type": "string"
                    },
                    "note": {
                      "type": "string"
                    },
                    "answers": {
                      "type": "array",
                      "items": [
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "string"
                            },
                            "picture": {
                              "type": "string"
                            },
                            "emoji": {
                              "type": "null"
                            },
                            "alignment": {
                              "type": "string"
                            },
                            "eventPropValue": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "text",
                            "picture",
                            "emoji",
                            "alignment",
                            "eventPropValue"
                          ]
                        },
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "string"
                            },
                            "picture": {
                              "type": "string"
                            },
                            "emoji": {
                              "type": "null"
                            },
                            "alignment": {
                              "type": "string"
                            },
                            "eventPropValue": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "text",
                            "picture",
                            "emoji",
                            "alignment",
                            "eventPropValue"
                          ]
                        },
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "string"
                            },
                            "picture": {
                              "type": "string"
                            },
                            "emoji": {
                              "type": "null"
                            },
                            "alignment": {
                              "type": "string"
                            },
                            "eventPropValue": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "text",
                            "picture",
                            "emoji",
                            "alignment",
                            "eventPropValue"
                          ]
                        },
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "string"
                            },
                            "picture": {
                              "type": "string"
                            },
                            "emoji": {
                              "type": "null"
                            },
                            "alignment": {
                              "type": "string"
                            },
                            "eventPropValue": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "text",
                            "picture",
                            "emoji",
                            "alignment",
                            "eventPropValue"
                          ]
                        },
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "string"
                            },
                            "picture": {
                              "type": "null"
                            },
                            "emoji": {
                              "type": "null"
                            },
                            "alignment": {
                              "type": "null"
                            },
                            "eventPropValue": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "text",
                            "picture",
                            "emoji",
                            "alignment",
                            "eventPropValue"
                          ]
                        },
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "string"
                            },
                            "picture": {
                              "type": "string"
                            },
                            "emoji": {
                              "type": "null"
                            },
                            "alignment": {
                              "type": "string"
                            },
                            "eventPropValue": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "text",
                            "picture",
                            "emoji",
                            "alignment",
                            "eventPropValue"
                          ]
                        },
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "string"
                            },
                            "picture": {
                              "type": "string"
                            },
                            "emoji": {
                              "type": "null"
                            },
                            "alignment": {
                              "type": "string"
                            },
                            "eventPropValue": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "text",
                            "picture",
                            "emoji",
                            "alignment",
                            "eventPropValue"
                          ]
                        },
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "string"
                            },
                            "picture": {
                              "type": "string"
                            },
                            "emoji": {
                              "type": "null"
                            },
                            "alignment": {
                              "type": "string"
                            },
                            "eventPropValue": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "text",
                            "picture",
                            "emoji",
                            "alignment",
                            "eventPropValue"
                          ]
                        },
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "string"
                            },
                            "picture": {
                              "type": "string"
                            },
                            "emoji": {
                              "type": "null"
                            },
                            "alignment": {
                              "type": "string"
                            },
                            "eventPropValue": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "text",
                            "picture",
                            "emoji",
                            "alignment",
                            "eventPropValue"
                          ]
                        },
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "string"
                            },
                            "picture": {
                              "type": "null"
                            },
                            "emoji": {
                              "type": "null"
                            },
                            "alignment": {
                              "type": "null"
                            },
                            "eventPropValue": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "text",
                            "picture",
                            "emoji",
                            "alignment",
                            "eventPropValue"
                          ]
                        }
                      ]
                    },
                    "subQuestions": {
                      "type": "array",
                      "items": {}
                    }
                  },
                  "required": [
                    "id",
                    "text",
                    "title",
                    "section",
                    "note",
                    "answers",
                    "subQuestions"
                  ]
                },
                {
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "string"
                    },
                    "text": {
                      "type": "string"
                    },
                    "title": {
                      "type": "null"
                    },
                    "section": {
                      "type": "string"
                    },
                    "note": {
                      "type": "null"
                    },
                    "answers": {
                      "type": "array",
                      "items": [
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "string"
                            },
                            "picture": {
                              "type": "null"
                            },
                            "emoji": {
                              "type": "string"
                            },
                            "alignment": {
                              "type": "string"
                            },
                            "eventPropValue": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "text",
                            "picture",
                            "emoji",
                            "alignment",
                            "eventPropValue"
                          ]
                        },
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "string"
                            },
                            "picture": {
                              "type": "null"
                            },
                            "emoji": {
                              "type": "string"
                            },
                            "alignment": {
                              "type": "string"
                            },
                            "eventPropValue": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "text",
                            "picture",
                            "emoji",
                            "alignment",
                            "eventPropValue"
                          ]
                        },
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "string"
                            },
                            "picture": {
                              "type": "null"
                            },
                            "emoji": {
                              "type": "string"
                            },
                            "alignment": {
                              "type": "string"
                            },
                            "eventPropValue": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "text",
                            "picture",
                            "emoji",
                            "alignment",
                            "eventPropValue"
                          ]
                        },
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "string"
                            },
                            "picture": {
                              "type": "null"
                            },
                            "emoji": {
                              "type": "string"
                            },
                            "alignment": {
                              "type": "string"
                            },
                            "eventPropValue": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "text",
                            "picture",
                            "emoji",
                            "alignment",
                            "eventPropValue"
                          ]
                        }
                      ]
                    },
                    "subQuestions": {
                      "type": "array",
                      "items": {}
                    }
                  },
                  "required": [
                    "id",
                    "text",
                    "title",
                    "section",
                    "note",
                    "answers",
                    "subQuestions"
                  ]
                },
                {
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "string"
                    },
                    "text": {
                      "type": "string"
                    },
                    "title": {
                      "type": "null"
                    },
                    "section": {
                      "type": "string"
                    },
                    "note": {
                      "type": "null"
                    },
                    "answers": {
                      "type": "array",
                      "items": [
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "string"
                            },
                            "picture": {
                              "type": "null"
                            },
                            "emoji": {
                              "type": "null"
                            },
                            "alignment": {
                              "type": "null"
                            },
                            "eventPropValue": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "text",
                            "picture",
                            "emoji",
                            "alignment",
                            "eventPropValue"
                          ]
                        },
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "string"
                            },
                            "picture": {
                              "type": "null"
                            },
                            "emoji": {
                              "type": "null"
                            },
                            "alignment": {
                              "type": "null"
                            },
                            "eventPropValue": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "text",
                            "picture",
                            "emoji",
                            "alignment",
                            "eventPropValue"
                          ]
                        },
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "string"
                            },
                            "picture": {
                              "type": "null"
                            },
                            "emoji": {
                              "type": "null"
                            },
                            "alignment": {
                              "type": "null"
                            },
                            "eventPropValue": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "text",
                            "picture",
                            "emoji",
                            "alignment",
                            "eventPropValue"
                          ]
                        }
                      ]
                    },
                    "subQuestions": {
                      "type": "array",
                      "items": {}
                    }
                  },
                  "required": [
                    "id",
                    "text",
                    "title",
                    "section",
                    "note",
                    "answers",
                    "subQuestions"
                  ]
                },
                {
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "string"
                    },
                    "text": {
                      "type": "string"
                    },
                    "title": {
                      "type": "null"
                    },
                    "section": {
                      "type": "string"
                    },
                    "note": {
                      "type": "null"
                    },
                    "answers": {
                      "type": "array",
                      "items": [
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "string"
                            },
                            "picture": {
                              "type": "null"
                            },
                            "emoji": {
                              "type": "string"
                            },
                            "alignment": {
                              "type": "string"
                            },
                            "eventPropValue": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "text",
                            "picture",
                            "emoji",
                            "alignment",
                            "eventPropValue"
                          ]
                        },
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "string"
                            },
                            "picture": {
                              "type": "null"
                            },
                            "emoji": {
                              "type": "string"
                            },
                            "alignment": {
                              "type": "string"
                            },
                            "eventPropValue": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "text",
                            "picture",
                            "emoji",
                            "alignment",
                            "eventPropValue"
                          ]
                        },
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "string"
                            },
                            "picture": {
                              "type": "null"
                            },
                            "emoji": {
                              "type": "string"
                            },
                            "alignment": {
                              "type": "string"
                            },
                            "eventPropValue": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "text",
                            "picture",
                            "emoji",
                            "alignment",
                            "eventPropValue"
                          ]
                        },
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "string"
                            },
                            "picture": {
                              "type": "null"
                            },
                            "emoji": {
                              "type": "null"
                            },
                            "alignment": {
                              "type": "null"
                            },
                            "eventPropValue": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "text",
                            "picture",
                            "emoji",
                            "alignment",
                            "eventPropValue"
                          ]
                        }
                      ]
                    },
                    "subQuestions": {
                      "type": "array",
                      "items": {}
                    }
                  },
                  "required": [
                    "id",
                    "text",
                    "title",
                    "section",
                    "note",
                    "answers",
                    "subQuestions"
                  ]
                },
                {
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "string"
                    },
                    "text": {
                      "type": "string"
                    },
                    "title": {
                      "type": "null"
                    },
                    "section": {
                      "type": "string"
                    },
                    "note": {
                      "type": "null"
                    },
                    "answers": {
                      "type": "array",
                      "items": [
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "string"
                            },
                            "picture": {
                              "type": "null"
                            },
                            "emoji": {
                              "type": "null"
                            },
                            "alignment": {
                              "type": "null"
                            },
                            "eventPropValue": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "text",
                            "picture",
                            "emoji",
                            "alignment",
                            "eventPropValue"
                          ]
                        },
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "string"
                            },
                            "picture": {
                              "type": "null"
                            },
                            "emoji": {
                              "type": "null"
                            },
                            "alignment": {
                              "type": "null"
                            },
                            "eventPropValue": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "text",
                            "picture",
                            "emoji",
                            "alignment",
                            "eventPropValue"
                          ]
                        },
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "string"
                            },
                            "picture": {
                              "type": "null"
                            },
                            "emoji": {
                              "type": "null"
                            },
                            "alignment": {
                              "type": "null"
                            },
                            "eventPropValue": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "text",
                            "picture",
                            "emoji",
                            "alignment",
                            "eventPropValue"
                          ]
                        },
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "string"
                            },
                            "picture": {
                              "type": "null"
                            },
                            "emoji": {
                              "type": "null"
                            },
                            "alignment": {
                              "type": "null"
                            },
                            "eventPropValue": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "text",
                            "picture",
                            "emoji",
                            "alignment",
                            "eventPropValue"
                          ]
                        }
                      ]
                    },
                    "subQuestions": {
                      "type": "array",
                      "items": {}
                    }
                  },
                  "required": [
                    "id",
                    "text",
                    "title",
                    "section",
                    "note",
                    "answers",
                    "subQuestions"
                  ]
                },
                {
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "string"
                    },
                    "text": {
                      "type": "string"
                    },
                    "title": {
                      "type": "null"
                    },
                    "section": {
                      "type": "string"
                    },
                    "note": {
                      "type": "string"
                    },
                    "answers": {
                      "type": "array",
                      "items": [
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "string"
                            },
                            "picture": {
                              "type": "string"
                            },
                            "emoji": {
                              "type": "null"
                            },
                            "alignment": {
                              "type": "string"
                            },
                            "eventPropValue": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "text",
                            "picture",
                            "emoji",
                            "alignment",
                            "eventPropValue"
                          ]
                        },
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "string"
                            },
                            "picture": {
                              "type": "string"
                            },
                            "emoji": {
                              "type": "null"
                            },
                            "alignment": {
                              "type": "string"
                            },
                            "eventPropValue": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "text",
                            "picture",
                            "emoji",
                            "alignment",
                            "eventPropValue"
                          ]
                        },
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "string"
                            },
                            "picture": {
                              "type": "string"
                            },
                            "emoji": {
                              "type": "null"
                            },
                            "alignment": {
                              "type": "string"
                            },
                            "eventPropValue": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "text",
                            "picture",
                            "emoji",
                            "alignment",
                            "eventPropValue"
                          ]
                        },
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "string"
                            },
                            "picture": {
                              "type": "string"
                            },
                            "emoji": {
                              "type": "null"
                            },
                            "alignment": {
                              "type": "string"
                            },
                            "eventPropValue": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "text",
                            "picture",
                            "emoji",
                            "alignment",
                            "eventPropValue"
                          ]
                        },
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "string"
                            },
                            "picture": {
                              "type": "null"
                            },
                            "emoji": {
                              "type": "null"
                            },
                            "alignment": {
                              "type": "null"
                            },
                            "eventPropValue": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "text",
                            "picture",
                            "emoji",
                            "alignment",
                            "eventPropValue"
                          ]
                        }
                      ]
                    },
                    "subQuestions": {
                      "type": "array",
                      "items": {}
                    }
                  },
                  "required": [
                    "id",
                    "text",
                    "title",
                    "section",
                    "note",
                    "answers",
                    "subQuestions"
                  ]
                },
                {
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "string"
                    },
                    "text": {
                      "type": "string"
                    },
                    "title": {
                      "type": "null"
                    },
                    "section": {
                      "type": "string"
                    },
                    "note": {
                      "type": "null"
                    },
                    "answers": {
                      "type": "array",
                      "items": [
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "string"
                            },
                            "picture": {
                              "type": "null"
                            },
                            "emoji": {
                              "type": "string"
                            },
                            "alignment": {
                              "type": "string"
                            },
                            "eventPropValue": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "text",
                            "picture",
                            "emoji",
                            "alignment",
                            "eventPropValue"
                          ]
                        },
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "string"
                            },
                            "picture": {
                              "type": "null"
                            },
                            "emoji": {
                              "type": "string"
                            },
                            "alignment": {
                              "type": "string"
                            },
                            "eventPropValue": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "text",
                            "picture",
                            "emoji",
                            "alignment",
                            "eventPropValue"
                          ]
                        },
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "string"
                            },
                            "picture": {
                              "type": "null"
                            },
                            "emoji": {
                              "type": "string"
                            },
                            "alignment": {
                              "type": "string"
                            },
                            "eventPropValue": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "text",
                            "picture",
                            "emoji",
                            "alignment",
                            "eventPropValue"
                          ]
                        },
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "string"
                            },
                            "picture": {
                              "type": "null"
                            },
                            "emoji": {
                              "type": "string"
                            },
                            "alignment": {
                              "type": "string"
                            },
                            "eventPropValue": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "text",
                            "picture",
                            "emoji",
                            "alignment",
                            "eventPropValue"
                          ]
                        }
                      ]
                    },
                    "subQuestions": {
                      "type": "array",
                      "items": {}
                    }
                  },
                  "required": [
                    "id",
                    "text",
                    "title",
                    "section",
                    "note",
                    "answers",
                    "subQuestions"
                  ]
                },
                {
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "string"
                    },
                    "text": {
                      "type": "string"
                    },
                    "title": {
                      "type": "null"
                    },
                    "section": {
                      "type": "string"
                    },
                    "note": {
                      "type": "null"
                    },
                    "answers": {
                      "type": "array",
                      "items": [
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "string"
                            },
                            "picture": {
                              "type": "null"
                            },
                            "emoji": {
                              "type": "null"
                            },
                            "alignment": {
                              "type": "null"
                            },
                            "eventPropValue": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "text",
                            "picture",
                            "emoji",
                            "alignment",
                            "eventPropValue"
                          ]
                        },
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "string"
                            },
                            "picture": {
                              "type": "null"
                            },
                            "emoji": {
                              "type": "null"
                            },
                            "alignment": {
                              "type": "null"
                            },
                            "eventPropValue": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "text",
                            "picture",
                            "emoji",
                            "alignment",
                            "eventPropValue"
                          ]
                        },
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "string"
                            },
                            "picture": {
                              "type": "null"
                            },
                            "emoji": {
                              "type": "null"
                            },
                            "alignment": {
                              "type": "null"
                            },
                            "eventPropValue": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "text",
                            "picture",
                            "emoji",
                            "alignment",
                            "eventPropValue"
                          ]
                        },
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "string"
                            },
                            "picture": {
                              "type": "null"
                            },
                            "emoji": {
                              "type": "null"
                            },
                            "alignment": {
                              "type": "null"
                            },
                            "eventPropValue": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "text",
                            "picture",
                            "emoji",
                            "alignment",
                            "eventPropValue"
                          ]
                        }
                      ]
                    },
                    "subQuestions": {
                      "type": "array",
                      "items": {}
                    }
                  },
                  "required": [
                    "id",
                    "text",
                    "title",
                    "section",
                    "note",
                    "answers",
                    "subQuestions"
                  ]
                },
                {
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "string"
                    },
                    "text": {
                      "type": "string"
                    },
                    "title": {
                      "type": "null"
                    },
                    "section": {
                      "type": "string"
                    },
                    "note": {
                      "type": "null"
                    },
                    "answers": {
                      "type": "array",
                      "items": [
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "string"
                            },
                            "picture": {
                              "type": "null"
                            },
                            "emoji": {
                              "type": "string"
                            },
                            "alignment": {
                              "type": "string"
                            },
                            "eventPropValue": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "text",
                            "picture",
                            "emoji",
                            "alignment",
                            "eventPropValue"
                          ]
                        },
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "string"
                            },
                            "picture": {
                              "type": "null"
                            },
                            "emoji": {
                              "type": "string"
                            },
                            "alignment": {
                              "type": "string"
                            },
                            "eventPropValue": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "text",
                            "picture",
                            "emoji",
                            "alignment",
                            "eventPropValue"
                          ]
                        },
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "string"
                            },
                            "picture": {
                              "type": "null"
                            },
                            "emoji": {
                              "type": "string"
                            },
                            "alignment": {
                              "type": "string"
                            },
                            "eventPropValue": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "text",
                            "picture",
                            "emoji",
                            "alignment",
                            "eventPropValue"
                          ]
                        },
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "string"
                            },
                            "picture": {
                              "type": "null"
                            },
                            "emoji": {
                              "type": "string"
                            },
                            "alignment": {
                              "type": "string"
                            },
                            "eventPropValue": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "text",
                            "picture",
                            "emoji",
                            "alignment",
                            "eventPropValue"
                          ]
                        }
                      ]
                    },
                    "subQuestions": {
                      "type": "array",
                      "items": {}
                    }
                  },
                  "required": [
                    "id",
                    "text",
                    "title",
                    "section",
                    "note",
                    "answers",
                    "subQuestions"
                  ]
                },
                {
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "string"
                    },
                    "text": {
                      "type": "string"
                    },
                    "title": {
                      "type": "null"
                    },
                    "section": {
                      "type": "string"
                    },
                    "note": {
                      "type": "string"
                    },
                    "answers": {
                      "type": "array",
                      "items": [
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "string"
                            },
                            "picture": {
                              "type": "null"
                            },
                            "emoji": {
                              "type": "string"
                            },
                            "alignment": {
                              "type": "string"
                            },
                            "eventPropValue": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "text",
                            "picture",
                            "emoji",
                            "alignment",
                            "eventPropValue"
                          ]
                        },
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "string"
                            },
                            "picture": {
                              "type": "null"
                            },
                            "emoji": {
                              "type": "string"
                            },
                            "alignment": {
                              "type": "string"
                            },
                            "eventPropValue": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "text",
                            "picture",
                            "emoji",
                            "alignment",
                            "eventPropValue"
                          ]
                        },
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "string"
                            },
                            "picture": {
                              "type": "null"
                            },
                            "emoji": {
                              "type": "string"
                            },
                            "alignment": {
                              "type": "string"
                            },
                            "eventPropValue": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "text",
                            "picture",
                            "emoji",
                            "alignment",
                            "eventPropValue"
                          ]
                        }
                      ]
                    },
                    "subQuestions": {
                      "type": "array",
                      "items": {}
                    }
                  },
                  "required": [
                    "id",
                    "text",
                    "title",
                    "section",
                    "note",
                    "answers",
                    "subQuestions"
                  ]
                },
                {
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "string"
                    },
                    "text": {
                      "type": "string"
                    },
                    "title": {
                      "type": "null"
                    },
                    "section": {
                      "type": "string"
                    },
                    "note": {
                      "type": "string"
                    },
                    "answers": {
                      "type": "array",
                      "items": [
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "string"
                            },
                            "picture": {
                              "type": "null"
                            },
                            "emoji": {
                              "type": "null"
                            },
                            "alignment": {
                              "type": "null"
                            },
                            "eventPropValue": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "text",
                            "picture",
                            "emoji",
                            "alignment",
                            "eventPropValue"
                          ]
                        },
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "string"
                            },
                            "picture": {
                              "type": "null"
                            },
                            "emoji": {
                              "type": "null"
                            },
                            "alignment": {
                              "type": "null"
                            },
                            "eventPropValue": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "text",
                            "picture",
                            "emoji",
                            "alignment",
                            "eventPropValue"
                          ]
                        },
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "string"
                            },
                            "picture": {
                              "type": "null"
                            },
                            "emoji": {
                              "type": "null"
                            },
                            "alignment": {
                              "type": "null"
                            },
                            "eventPropValue": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "text",
                            "picture",
                            "emoji",
                            "alignment",
                            "eventPropValue"
                          ]
                        },
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "string"
                            },
                            "picture": {
                              "type": "null"
                            },
                            "emoji": {
                              "type": "null"
                            },
                            "alignment": {
                              "type": "null"
                            },
                            "eventPropValue": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "text",
                            "picture",
                            "emoji",
                            "alignment",
                            "eventPropValue"
                          ]
                        },
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "string"
                            },
                            "picture": {
                              "type": "null"
                            },
                            "emoji": {
                              "type": "null"
                            },
                            "alignment": {
                              "type": "null"
                            },
                            "eventPropValue": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "text",
                            "picture",
                            "emoji",
                            "alignment",
                            "eventPropValue"
                          ]
                        },
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "string"
                            },
                            "picture": {
                              "type": "null"
                            },
                            "emoji": {
                              "type": "null"
                            },
                            "alignment": {
                              "type": "null"
                            },
                            "eventPropValue": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "text",
                            "picture",
                            "emoji",
                            "alignment",
                            "eventPropValue"
                          ]
                        },
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "string"
                            },
                            "picture": {
                              "type": "null"
                            },
                            "emoji": {
                              "type": "null"
                            },
                            "alignment": {
                              "type": "null"
                            },
                            "eventPropValue": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "text",
                            "picture",
                            "emoji",
                            "alignment",
                            "eventPropValue"
                          ]
                        },
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "string"
                            },
                            "picture": {
                              "type": "null"
                            },
                            "emoji": {
                              "type": "null"
                            },
                            "alignment": {
                              "type": "null"
                            },
                            "eventPropValue": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "text",
                            "picture",
                            "emoji",
                            "alignment",
                            "eventPropValue"
                          ]
                        },
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "string"
                            },
                            "picture": {
                              "type": "null"
                            },
                            "emoji": {
                              "type": "null"
                            },
                            "alignment": {
                              "type": "null"
                            },
                            "eventPropValue": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "text",
                            "picture",
                            "emoji",
                            "alignment",
                            "eventPropValue"
                          ]
                        },
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "string"
                            },
                            "picture": {
                              "type": "null"
                            },
                            "emoji": {
                              "type": "null"
                            },
                            "alignment": {
                              "type": "null"
                            },
                            "eventPropValue": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "text",
                            "picture",
                            "emoji",
                            "alignment",
                            "eventPropValue"
                          ]
                        },
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "string"
                            },
                            "picture": {
                              "type": "null"
                            },
                            "emoji": {
                              "type": "null"
                            },
                            "alignment": {
                              "type": "null"
                            },
                            "eventPropValue": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "text",
                            "picture",
                            "emoji",
                            "alignment",
                            "eventPropValue"
                          ]
                        }
                      ]
                    },
                    "subQuestions": {
                      "type": "array",
                      "items": {}
                    }
                  },
                  "required": [
                    "id",
                    "text",
                    "title",
                    "section",
                    "note",
                    "answers",
                    "subQuestions"
                  ]
                },
                {
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "string"
                    },
                    "text": {
                      "type": "string"
                    },
                    "title": {
                      "type": "null"
                    },
                    "section": {
                      "type": "string"
                    },
                    "note": {
                      "type": "null"
                    },
                    "answers": {
                      "type": "array",
                      "items": [
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "null"
                            },
                            "picture": {
                              "type": "null"
                            },
                            "emoji": {
                              "type": "string"
                            },
                            "alignment": {
                              "type": "string"
                            },
                            "eventPropValue": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "text",
                            "picture",
                            "emoji",
                            "alignment",
                            "eventPropValue"
                          ]
                        },
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "null"
                            },
                            "picture": {
                              "type": "null"
                            },
                            "emoji": {
                              "type": "string"
                            },
                            "alignment": {
                              "type": "string"
                            },
                            "eventPropValue": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "text",
                            "picture",
                            "emoji",
                            "alignment",
                            "eventPropValue"
                          ]
                        },
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "null"
                            },
                            "picture": {
                              "type": "null"
                            },
                            "emoji": {
                              "type": "string"
                            },
                            "alignment": {
                              "type": "string"
                            },
                            "eventPropValue": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "text",
                            "picture",
                            "emoji",
                            "alignment",
                            "eventPropValue"
                          ]
                        },
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "null"
                            },
                            "picture": {
                              "type": "null"
                            },
                            "emoji": {
                              "type": "string"
                            },
                            "alignment": {
                              "type": "string"
                            },
                            "eventPropValue": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "text",
                            "picture",
                            "emoji",
                            "alignment",
                            "eventPropValue"
                          ]
                        },
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "null"
                            },
                            "picture": {
                              "type": "null"
                            },
                            "emoji": {
                              "type": "string"
                            },
                            "alignment": {
                              "type": "string"
                            },
                            "eventPropValue": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "text",
                            "picture",
                            "emoji",
                            "alignment",
                            "eventPropValue"
                          ]
                        }
                      ]
                    },
                    "subQuestions": {
                      "type": "array",
                      "items": {}
                    }
                  },
                  "required": [
                    "id",
                    "text",
                    "title",
                    "section",
                    "note",
                    "answers",
                    "subQuestions"
                  ]
                },
                {
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "string"
                    },
                    "text": {
                      "type": "string"
                    },
                    "title": {
                      "type": "null"
                    },
                    "section": {
                      "type": "string"
                    },
                    "note": {
                      "type": "string"
                    },
                    "answers": {
                      "type": "array",
                      "items": [
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "string"
                            },
                            "picture": {
                              "type": "string"
                            },
                            "emoji": {
                              "type": "null"
                            },
                            "alignment": {
                              "type": "string"
                            },
                            "eventPropValue": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "text",
                            "picture",
                            "emoji",
                            "alignment",
                            "eventPropValue"
                          ]
                        },
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "string"
                            },
                            "picture": {
                              "type": "string"
                            },
                            "emoji": {
                              "type": "null"
                            },
                            "alignment": {
                              "type": "string"
                            },
                            "eventPropValue": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "text",
                            "picture",
                            "emoji",
                            "alignment",
                            "eventPropValue"
                          ]
                        },
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "string"
                            },
                            "picture": {
                              "type": "string"
                            },
                            "emoji": {
                              "type": "null"
                            },
                            "alignment": {
                              "type": "string"
                            },
                            "eventPropValue": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "text",
                            "picture",
                            "emoji",
                            "alignment",
                            "eventPropValue"
                          ]
                        },
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "string"
                            },
                            "picture": {
                              "type": "string"
                            },
                            "emoji": {
                              "type": "null"
                            },
                            "alignment": {
                              "type": "string"
                            },
                            "eventPropValue": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "text",
                            "picture",
                            "emoji",
                            "alignment",
                            "eventPropValue"
                          ]
                        },
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "string"
                            },
                            "picture": {
                              "type": "string"
                            },
                            "emoji": {
                              "type": "null"
                            },
                            "alignment": {
                              "type": "string"
                            },
                            "eventPropValue": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "text",
                            "picture",
                            "emoji",
                            "alignment",
                            "eventPropValue"
                          ]
                        },
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "string"
                            },
                            "picture": {
                              "type": "string"
                            },
                            "emoji": {
                              "type": "null"
                            },
                            "alignment": {
                              "type": "string"
                            },
                            "eventPropValue": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "text",
                            "picture",
                            "emoji",
                            "alignment",
                            "eventPropValue"
                          ]
                        },
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "string"
                            },
                            "picture": {
                              "type": "string"
                            },
                            "emoji": {
                              "type": "null"
                            },
                            "alignment": {
                              "type": "string"
                            },
                            "eventPropValue": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "text",
                            "picture",
                            "emoji",
                            "alignment",
                            "eventPropValue"
                          ]
                        },
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "string"
                            },
                            "picture": {
                              "type": "string"
                            },
                            "emoji": {
                              "type": "null"
                            },
                            "alignment": {
                              "type": "string"
                            },
                            "eventPropValue": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "text",
                            "picture",
                            "emoji",
                            "alignment",
                            "eventPropValue"
                          ]
                        },
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "string"
                            },
                            "picture": {
                              "type": "string"
                            },
                            "emoji": {
                              "type": "null"
                            },
                            "alignment": {
                              "type": "string"
                            },
                            "eventPropValue": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "text",
                            "picture",
                            "emoji",
                            "alignment",
                            "eventPropValue"
                          ]
                        },
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "string"
                            },
                            "picture": {
                              "type": "string"
                            },
                            "emoji": {
                              "type": "null"
                            },
                            "alignment": {
                              "type": "string"
                            },
                            "eventPropValue": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "text",
                            "picture",
                            "emoji",
                            "alignment",
                            "eventPropValue"
                          ]
                        },
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "string"
                            },
                            "picture": {
                              "type": "string"
                            },
                            "emoji": {
                              "type": "null"
                            },
                            "alignment": {
                              "type": "string"
                            },
                            "eventPropValue": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "text",
                            "picture",
                            "emoji",
                            "alignment",
                            "eventPropValue"
                          ]
                        },
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "string"
                            },
                            "picture": {
                              "type": "string"
                            },
                            "emoji": {
                              "type": "null"
                            },
                            "alignment": {
                              "type": "string"
                            },
                            "eventPropValue": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "text",
                            "picture",
                            "emoji",
                            "alignment",
                            "eventPropValue"
                          ]
                        }
                      ]
                    },
                    "subQuestions": {
                      "type": "array",
                      "items": {}
                    }
                  },
                  "required": [
                    "id",
                    "text",
                    "title",
                    "section",
                    "note",
                    "answers",
                    "subQuestions"
                  ]
                },
                {
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "string"
                    },
                    "text": {
                      "type": "string"
                    },
                    "title": {
                      "type": "null"
                    },
                    "section": {
                      "type": "string"
                    },
                    "note": {
                      "type": "null"
                    },
                    "answers": {
                      "type": "array",
                      "items": [
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "null"
                            },
                            "picture": {
                              "type": "null"
                            },
                            "emoji": {
                              "type": "string"
                            },
                            "alignment": {
                              "type": "string"
                            },
                            "eventPropValue": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "text",
                            "picture",
                            "emoji",
                            "alignment",
                            "eventPropValue"
                          ]
                        },
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "null"
                            },
                            "picture": {
                              "type": "null"
                            },
                            "emoji": {
                              "type": "string"
                            },
                            "alignment": {
                              "type": "string"
                            },
                            "eventPropValue": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "text",
                            "picture",
                            "emoji",
                            "alignment",
                            "eventPropValue"
                          ]
                        },
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "null"
                            },
                            "picture": {
                              "type": "null"
                            },
                            "emoji": {
                              "type": "string"
                            },
                            "alignment": {
                              "type": "string"
                            },
                            "eventPropValue": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "text",
                            "picture",
                            "emoji",
                            "alignment",
                            "eventPropValue"
                          ]
                        },
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "null"
                            },
                            "picture": {
                              "type": "null"
                            },
                            "emoji": {
                              "type": "string"
                            },
                            "alignment": {
                              "type": "string"
                            },
                            "eventPropValue": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "text",
                            "picture",
                            "emoji",
                            "alignment",
                            "eventPropValue"
                          ]
                        },
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "null"
                            },
                            "picture": {
                              "type": "null"
                            },
                            "emoji": {
                              "type": "string"
                            },
                            "alignment": {
                              "type": "string"
                            },
                            "eventPropValue": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "text",
                            "picture",
                            "emoji",
                            "alignment",
                            "eventPropValue"
                          ]
                        }
                      ]
                    },
                    "subQuestions": {
                      "type": "array",
                      "items": {}
                    }
                  },
                  "required": [
                    "id",
                    "text",
                    "title",
                    "section",
                    "note",
                    "answers",
                    "subQuestions"
                  ]
                },
                {
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "string"
                    },
                    "text": {
                      "type": "string"
                    },
                    "title": {
                      "type": "string"
                    },
                    "section": {
                      "type": "string"
                    },
                    "note": {
                      "type": "null"
                    },
                    "answers": {
                      "type": "array",
                      "items": {}
                    },
                    "subQuestions": {
                      "type": "array",
                      "items": {}
                    }
                  },
                  "required": [
                    "id",
                    "text",
                    "title",
                    "section",
                    "note",
                    "answers",
                    "subQuestions"
                  ]
                },
                {
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "string"
                    },
                    "text": {
                      "type": "string"
                    },
                    "title": {
                      "type": "null"
                    },
                    "section": {
                      "type": "string"
                    },
                    "note": {
                      "type": "string"
                    },
                    "answers": {
                      "type": "array",
                      "items": [
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "string"
                            },
                            "picture": {
                              "type": "null"
                            },
                            "emoji": {
                              "type": "string"
                            },
                            "alignment": {
                              "type": "string"
                            },
                            "eventPropValue": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "text",
                            "picture",
                            "emoji",
                            "alignment",
                            "eventPropValue"
                          ]
                        },
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "string"
                            },
                            "picture": {
                              "type": "null"
                            },
                            "emoji": {
                              "type": "string"
                            },
                            "alignment": {
                              "type": "string"
                            },
                            "eventPropValue": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "text",
                            "picture",
                            "emoji",
                            "alignment",
                            "eventPropValue"
                          ]
                        },
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "string"
                            },
                            "picture": {
                              "type": "null"
                            },
                            "emoji": {
                              "type": "string"
                            },
                            "alignment": {
                              "type": "string"
                            },
                            "eventPropValue": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "text",
                            "picture",
                            "emoji",
                            "alignment",
                            "eventPropValue"
                          ]
                        },
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "string"
                            },
                            "picture": {
                              "type": "null"
                            },
                            "emoji": {
                              "type": "string"
                            },
                            "alignment": {
                              "type": "string"
                            },
                            "eventPropValue": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "text",
                            "picture",
                            "emoji",
                            "alignment",
                            "eventPropValue"
                          ]
                        },
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "string"
                            },
                            "picture": {
                              "type": "null"
                            },
                            "emoji": {
                              "type": "string"
                            },
                            "alignment": {
                              "type": "string"
                            },
                            "eventPropValue": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "text",
                            "picture",
                            "emoji",
                            "alignment",
                            "eventPropValue"
                          ]
                        },
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "string"
                            },
                            "picture": {
                              "type": "null"
                            },
                            "emoji": {
                              "type": "null"
                            },
                            "alignment": {
                              "type": "null"
                            },
                            "eventPropValue": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "text",
                            "picture",
                            "emoji",
                            "alignment",
                            "eventPropValue"
                          ]
                        }
                      ]
                    },
                    "subQuestions": {
                      "type": "array",
                      "items": {}
                    }
                  },
                  "required": [
                    "id",
                    "text",
                    "title",
                    "section",
                    "note",
                    "answers",
                    "subQuestions"
                  ]
                },
                {
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "string"
                    },
                    "text": {
                      "type": "string"
                    },
                    "title": {
                      "type": "null"
                    },
                    "section": {
                      "type": "string"
                    },
                    "note": {
                      "type": "null"
                    },
                    "answers": {
                      "type": "array",
                      "items": [
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "string"
                            },
                            "picture": {
                              "type": "null"
                            },
                            "emoji": {
                              "type": "null"
                            },
                            "alignment": {
                              "type": "null"
                            },
                            "eventPropValue": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "text",
                            "picture",
                            "emoji",
                            "alignment",
                            "eventPropValue"
                          ]
                        },
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "string"
                            },
                            "picture": {
                              "type": "null"
                            },
                            "emoji": {
                              "type": "null"
                            },
                            "alignment": {
                              "type": "null"
                            },
                            "eventPropValue": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "text",
                            "picture",
                            "emoji",
                            "alignment",
                            "eventPropValue"
                          ]
                        },
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "string"
                            },
                            "picture": {
                              "type": "null"
                            },
                            "emoji": {
                              "type": "null"
                            },
                            "alignment": {
                              "type": "null"
                            },
                            "eventPropValue": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "text",
                            "picture",
                            "emoji",
                            "alignment",
                            "eventPropValue"
                          ]
                        },
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "string"
                            },
                            "picture": {
                              "type": "null"
                            },
                            "emoji": {
                              "type": "null"
                            },
                            "alignment": {
                              "type": "null"
                            },
                            "eventPropValue": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "text",
                            "picture",
                            "emoji",
                            "alignment",
                            "eventPropValue"
                          ]
                        },
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "string"
                            },
                            "picture": {
                              "type": "null"
                            },
                            "emoji": {
                              "type": "null"
                            },
                            "alignment": {
                              "type": "null"
                            },
                            "eventPropValue": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "text",
                            "picture",
                            "emoji",
                            "alignment",
                            "eventPropValue"
                          ]
                        }
                      ]
                    },
                    "subQuestions": {
                      "type": "array",
                      "items": {}
                    }
                  },
                  "required": [
                    "id",
                    "text",
                    "title",
                    "section",
                    "note",
                    "answers",
                    "subQuestions"
                  ]
                },
                {
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "string"
                    },
                    "text": {
                      "type": "string"
                    },
                    "title": {
                      "type": "null"
                    },
                    "section": {
                      "type": "string"
                    },
                    "note": {
                      "type": "string"
                    },
                    "answers": {
                      "type": "array",
                      "items": [
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "string"
                            },
                            "picture": {
                              "type": "null"
                            },
                            "emoji": {
                              "type": "null"
                            },
                            "alignment": {
                              "type": "null"
                            },
                            "eventPropValue": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "text",
                            "picture",
                            "emoji",
                            "alignment",
                            "eventPropValue"
                          ]
                        },
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "string"
                            },
                            "picture": {
                              "type": "null"
                            },
                            "emoji": {
                              "type": "null"
                            },
                            "alignment": {
                              "type": "null"
                            },
                            "eventPropValue": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "text",
                            "picture",
                            "emoji",
                            "alignment",
                            "eventPropValue"
                          ]
                        },
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "string"
                            },
                            "picture": {
                              "type": "null"
                            },
                            "emoji": {
                              "type": "null"
                            },
                            "alignment": {
                              "type": "null"
                            },
                            "eventPropValue": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "text",
                            "picture",
                            "emoji",
                            "alignment",
                            "eventPropValue"
                          ]
                        },
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "string"
                            },
                            "picture": {
                              "type": "null"
                            },
                            "emoji": {
                              "type": "null"
                            },
                            "alignment": {
                              "type": "null"
                            },
                            "eventPropValue": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "text",
                            "picture",
                            "emoji",
                            "alignment",
                            "eventPropValue"
                          ]
                        },
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "string"
                            },
                            "picture": {
                              "type": "null"
                            },
                            "emoji": {
                              "type": "null"
                            },
                            "alignment": {
                              "type": "null"
                            },
                            "eventPropValue": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "text",
                            "picture",
                            "emoji",
                            "alignment",
                            "eventPropValue"
                          ]
                        }
                      ]
                    },
                    "subQuestions": {
                      "type": "array",
                      "items": {}
                    }
                  },
                  "required": [
                    "id",
                    "text",
                    "title",
                    "section",
                    "note",
                    "answers",
                    "subQuestions"
                  ]
                },
                {
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "string"
                    },
                    "text": {
                      "type": "string"
                    },
                    "title": {
                      "type": "string"
                    },
                    "section": {
                      "type": "string"
                    },
                    "note": {
                      "type": "null"
                    },
                    "answers": {
                      "type": "array",
                      "items": {}
                    },
                    "subQuestions": {
                      "type": "array",
                      "items": [
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "string"
                            },
                            "id": {
                              "type": "string"
                            },
                            "title": {
                              "type": "string"
                            },
                            "modifier": {
                              "type": "null"
                            },
                            "identifier": {
                              "type": "null"
                            },
                            "event": {
                              "type": "string"
                            },
                            "eventProp": {
                              "type": "string"
                            },
                            "section": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "text",
                            "id",
                            "title",
                            "modifier",
                            "identifier",
                            "event",
                            "eventProp",
                            "section"
                          ]
                        },
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "string"
                            },
                            "id": {
                              "type": "string"
                            },
                            "title": {
                              "type": "string"
                            },
                            "modifier": {
                              "type": "null"
                            },
                            "identifier": {
                              "type": "null"
                            },
                            "event": {
                              "type": "string"
                            },
                            "eventProp": {
                              "type": "string"
                            },
                            "section": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "text",
                            "id",
                            "title",
                            "modifier",
                            "identifier",
                            "event",
                            "eventProp",
                            "section"
                          ]
                        },
                        {
                          "type": "object",
                          "properties": {
                            "text": {
                              "type": "string"
                            },
                            "id": {
                              "type": "string"
                            },
                            "title": {
                              "type": "string"
                            },
                            "modifier": {
                              "type": "null"
                            },
                            "identifier": {
                              "type": "null"
                            },
                            "event": {
                              "type": "string"
                            },
                            "eventProp": {
                              "type": "string"
                            },
                            "section": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "text",
                            "id",
                            "title",
                            "modifier",
                            "identifier",
                            "event",
                            "eventProp",
                            "section"
                          ]
                        }
                      ]
                    }
                  },
                  "required": [
                    "id",
                    "text",
                    "title",
                    "section",
                    "note",
                    "answers",
                    "subQuestions"
                  ]
                }
              ]
            }
          },
          "required": [
            "onboardingQuestions"
          ]
        }
      },
      "required": [
        "viewer"
      ]
    }
  },
  "required": [
    "data"
  ]
}


PLANS_VIP = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "data": {
      "type": "object",
      "properties": {
        "viewer": {
          "type": "object",
          "properties": {
            "profile": {
              "type": "object",
              "properties": {
                "id": {
                  "type": "string"
                },
                "email": {
                  "type": "string"
                },
                "plans": {
                  "type": "array",
                  "items": [
                    {
                      "type": "object",
                      "properties": {
                        "id": {
                          "type": "string"
                        },
                        "planId": {
                          "type": "string"
                        },
                        "gateway": {
                          "type": "string"
                        },
                        "type": {
                          "type": "string"
                        },
                        "purchaseType": {
                          "type": "string"
                        },
                        "priceLevel": {
                          "type": "integer"
                        },
                        "currency": {
                          "type": "string"
                        },
                        "price": {
                          "type": "number"
                        },
                        "priceRecurring": {
                          "type": "null"
                        },
                        "fullPrice": {
                          "type": "number"
                        },
                        "discountPercent": {
                          "type": "integer"
                        },
                        "needShowDiscount": {
                          "type": "boolean"
                        },
                        "durationText": {
                          "type": "string"
                        },
                        "titleText": {
                          "type": "string"
                        }
                      },
                      "required": [
                        "id",
                        "planId",
                        "gateway",
                        "type",
                        "purchaseType",
                        "priceLevel",
                        "currency",
                        "price",
                        "priceRecurring",
                        "fullPrice",
                        "discountPercent",
                        "needShowDiscount",
                        "durationText",
                        "titleText"
                      ]
                    }
                  ]
                }
              },
              "required": [
                "id",
                "email",
                "plans"
              ]
            }
          },
          "required": [
            "profile"
          ]
        }
      },
      "required": [
        "viewer"
      ]
    }
  },
  "required": [
    "data"
  ]
}